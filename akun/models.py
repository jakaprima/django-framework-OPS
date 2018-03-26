from django.db import models

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
from django.contrib.auth.models import PermissionsMixin
from core.models import TimeStampedModel

from datetime import timedelta
from django.utils import timezone
from django.conf import settings

from django.db.models.signals import pre_save, post_save
from .utils import unique_key_generator

from django.core.mail import send_mail

from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.template.loader import get_template


# Create your models here.

class Kontak(models.Model):
	nama_lengkap = models.CharField(max_length=255)
	email = models.EmailField()
	isi_pesan = models.CharField(max_length=255)

	def get_absolute_url(self):
		return reverse('blog:tentang-kami')


# class CobaManager(BaseUserManager):
#     def create_user(self, email, full_name=None, password=None, is_active=True, is_staff=False, is_admin=False):
#         if not email:
#             raise ValueError("Users must have an email address")
#         if not password:
#             raise ValueError("Users must have a password")
#         user_obj = self.model(
#             email = self.normalize_email(email),
#             full_name=full_name
#         )
#         user_obj.set_password(password) # change user password
#         user_obj.staff = is_staff
#         user_obj.admin = is_admin
#         user_obj.is_active = is_active
#         user_obj.save(using=self._db)
#         return user_obj

#     def create_staffuser(self, email,full_name=None, password=None):
#         user = self.create_user(
#                 email,
#                 full_name=full_name,
#                 password=password,
#                 is_staff=True
#         )
#         return user

#     def create_superuser(self, email, full_name=None, password=None):
#         user = self.create_user(
#                 email,
#                 full_name=full_name,
#                 password=password,
#                 is_staff=True,
#                 is_admin=True
#         )
#         return user


# class Coba(AbstractBaseUser):
#     email       = models.EmailField(max_length=255, unique=True)
#     full_name   = models.CharField(max_length=255, blank=True, null=True)
#     is_active   = models.BooleanField(default=True) # can login 
#     staff       = models.BooleanField(default=False) # staff user non superuser
#     admin       = models.BooleanField(default=False) # superuser 
#     timestamp   = models.DateTimeField(auto_now_add=True)
#     # confirm     = models.BooleanField(default=False)
#     # confirmed_date     = models.DateTimeField(default=False)

#     USERNAME_FIELD = 'email' #username
#     # USERNAME_FIELD and password are required by default
#     REQUIRED_FIELDS = [] #['full_name'] #python manage.py createsuperuser

#     objects = CobaManager()

#     def __str__(self):
#         return self.email

#     def get_full_name(self):
#         if self.full_name:
#             return self.full_name
#         return self.email

#     def get_short_name(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True

#     @property
#     def is_staff(self):
#         if self.is_admin:
#             return True
#         return self.staff

#     @property
#     def is_admin(self):
#         return self.admin

#     # @property
#     # def is_active(self):
#     #     return self.active




# 2. buat custom manager
class AkunManager(BaseUserManager):
	# semua yang di required field di akun object akan menjadi params di bawah ini
	def create_user(self, email, tanggal_lahir, password=None):
	    """
	    membuat dan menyimpan User dengan email tanggal lahir dan password
	    """
	    if not email:
	        raise ValueError('User harus punya email address')

	    user = self.model(
	        email=self.normalize_email(email),
	        tanggal_lahir=tanggal_lahir,
	    )

	    user.set_password(password)
	    user.save(using=self._db)
	    return user

	def create_superuser(self, email, tanggal_lahir, password):
	    """
	    membuat dan menyimpan superuser dengan email yang diberikan, tanggal lahir dan password.
	    """
	    user = self.create_user(email,
	        password=password,
	        tanggal_lahir=tanggal_lahir
	    )
	    user.is_admin = True
	    user.save(using=self._db)
	    return user

# 1. abstrak user yang akan dibuat
class Akun(AbstractBaseUser):
	email = models.EmailField(
			verbose_name='alamat email',
			max_length=255, 
			unique=True
		)
	nama_lengkap = models.CharField(max_length=255, blank=True, null=True)
	tanggal_lahir = models.DateField()
	is_active = models.BooleanField(default=True) #bisa login
	is_staff = models.BooleanField(default=False) #staff bukan superuser
	is_admin = models.BooleanField(default=False) #superuser

	USERNAME_FIELD = 'email' #mengisi username field di default django dengan email
	REQUIRED_FIELDS = ['tanggal_lahir'] #yang required misal ['tanggal_lahir'] ketika ./manage.py createsuperuser ini akan required

	objects = AkunManager()

	def get_full_name(self):
	    # user mengidentifikasi dengan nama email mereka
	    return self.email

	def get_short_name(self):
	    # User mengidentifikasi dengan alamat emailnya
	    return self.email

	def __str__(self):              # __unicode__ on Python 2
	    return self.email

	def has_perm(self, perm, obj=None):
	    # "apakah user memiliki spesifik permission?"
	    # jawaban yang simple adalah ya, selalu
	    return True

	def has_module_perms(self, app_label):
	    "apakah user memiliki permission untuk view app ``app_label?"
	    # ya selalu
	    return True

	@property
	def is_staff(self):
	    "apakah user member dari staff?"
	    # semua admin adalah staff
	    return self.is_admin




# ________________________
# USER AKTIVASI
# ________________________
DEFAULT_ACTIVATION_DAYS = getattr(settings, 'DEFAULT_ACTIVATION_DAYS', 7)
class AktivasiEmailQuerySet(models.query.QuerySet):
	def aksikonfirmasi(self):
		sekarang = timezone.now()
		range_awal = sekarang - timedelta(days=DEFAULT_ACTIVATION_DAYS)
		range_akhir = sekarang
		return self.filter(
			activated = False,
			forced_expired = False
			).filter(created_at__gt=range_awal, updated_at__lte=range_akhir)


class AktivasiEmailManager(models.Manager):
	def get_queryset(self):
		return AktivasiEmailQuerySet(self.model, using=self._db)
	def aksikonfirmasi(self):
		return self.get_queryset().aksikonfirmasi()

	def ada_email(self, email):
		return self.get_queryset().filter(
				Q(email=email) |
				Q(user__email=email)
			).filter(
				activated=False
			)




class AktivasiEmail(TimeStampedModel):
	user = models.ForeignKey(Akun)
	email = models.EmailField()
	key = models.CharField(
		max_length=120,
		blank=True,
		null=True
	)
	activated = models.BooleanField(
		default=False
	)
	forced_expired = models.BooleanField(
		default=False
	)
	expires = models.IntegerField(
		default=7
	)

	objects = AktivasiEmailManager()

	def __str__(self):
		return self.email

	def bisa_aktivasi(self):
		qs = AktivasiEmail.objects.filter(pk=self.pk).aksikonfirmasi()
		if qs.exists():
			return True
		return False

	def aktivasi_akun(self):
		if self.bisa_aktivasi():
			user = self.user
			user.is_active = True
			user.save()

			self.activated = True
			self.save()
			return True
		return False

	def regenerate(self):
		self.key = None
		self.save()
		if self.key is not None:
			return True
		return False

	# tereksekusi saat pre_save
	def kirim_email_aktivasi(self):
	    if not self.activated and not self.forced_expired:
	        if self.key:
	            base_url = getattr(settings, 'BASE_URL', '127.0.0.1:8000')
	            key_path = reverse("akun:kirim-aktivasi", kwargs={'key': self.key}) # use reverse
	            path = "{base}{path}".format(base=base_url, path=key_path)
	            context = {
	                'path': path,
	                'email': self.email
	            }
	            txt_ = get_template("registration/emails/verify.txt").render(context)
	            html_ = get_template("registration/emails/verify.html").render(context)
	            subject = '1-Click Email Verification'
	            from_email = settings.DEFAULT_FROM_EMAIL
	            recipient_list = [self.email]
	            sent_mail = send_mail(
	                        subject,
	                        txt_,
	                        from_email,
	                        recipient_list,
	                        html_message=html_,
	                        fail_silently=False,
	                )
	            return sent_mail
	    return False


# terkirim pada awal model save() method.
def pre_save_aktivasi_email(sender, instance, *args, **kwargs):

	if not instance.activated and not instance.forced_expired:
		if not instance.key:
			instance.key = unique_key_generator(instance)

pre_save.connect(pre_save_aktivasi_email, sender=AktivasiEmail)

# seperti pre_save, tetapi terkirim pada akhir save() method.
def post_save_membuat_aktivasi(sender, instance, created, *args, **kwargs):
	if created:
		obj = AktivasiEmail.objects.create(user=instance, email=instance.email)
		obj.kirim_email_aktivasi()
post_save.connect(post_save_membuat_aktivasi, sender=Akun)






