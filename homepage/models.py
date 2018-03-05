from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models import Count
from tinymce.models import HTMLField

from django.core.urlresolvers import reverse

# Create your models here.
class SettingWeb(models.Model):
	nama_web = models.CharField(max_length=35)
	deskripsi_web = models.CharField(max_length=60)
	def __str__(self):
		return self.nama_web

class Kategori(models.Model):
	nama_kategori = models.CharField(max_length=25)
	slug = models.SlugField(unique=True, null=True)

	def __str__(self):
		return self.nama_kategori

def create_slug(instance, new_slug=None):
	slug = slugify(instance.nama_kategori)
	if new_slug is not None:
		slug = new_slug
	qs = Kategori.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)
	#exe membuat slg
	pre_save.connect(pre_save_post_receiver, sender=Orang)



class Artikel(models.Model):
	penulis = models.ForeignKey(User, null=True, blank=True)
	judul_artikel = models.CharField(max_length=200)
	kategori_artikel = models.ManyToManyField(Kategori, null=True, blank=True, related_name='kategori_related') #biar bisa di pake di template
	# komentar_artikel = models.ManyToManyField('Komentar', blank=True, null=True, through='Postlist')
	isi_artikel = HTMLField()
	created_at = models.DateTimeField(default=timezone.now)
	updated_at = models.DateTimeField(blank=True, null=True)


	# ----- fungsi action --------- #
	def tampilkan_post(self):
		self.published_date = timezone.now()
		self.save()

	def izin_komentar(self):
		return self.komentar.filter(izin_komentar=True)

	# ----- fungsi action --------- #
	def __str__(self): # biar di admin rownya tidak kata kata object tapi sesuai isi
		return str(self.judul_artikel)

class Komentar(models.Model):
	artikel = models.ForeignKey(Artikel, null=True, blank=True)
	penulis_komentar = models.ForeignKey(User, null=True, blank=True)
	isi_komentar = models.CharField(max_length=200)
	created_at = models.DateTimeField(default=timezone.now)
	updated_at = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.isi_komentar
		# return '(artikel) '+ str(self.artikel) + ' (komentar) ' + str(self.isi_komentar)

# class Postlist(models.Model):
# 	penulis_id = models.ForeignKey(User, null=True, blank=True)
# 	artikel_id = models.ForeignKey(Artikel, null=True, blank=True)
# 	komentar_id = models.ForeignKey(Komentar, null=True, blank=True)

# 	def __str__(self):
# 		return str(self.komentar_id) + str(self.artikel_id)

class Penulis(models.Model):
	nama = models.CharField(max_length=200)
	email = models.EmailField()

	def __str__(self):
		return self.nama

class Kontak(models.Model):
	nama_lengkap = models.CharField(max_length=255)
	email = models.EmailField()
	isi_pesan = models.CharField(max_length=255)

	def get_absolute_url(self):
		return reverse('homepage:tentang-kami')



