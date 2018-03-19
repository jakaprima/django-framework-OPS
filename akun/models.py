from django.db import models

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
from core.models import TimeStampedModel

# Create your models here.

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
		return reverse('blog:tentang-kami')



class User(AbstractBaseUser):
	email = models.EmailField(max_length=255, unique=True)
	nama_lengkap = models.CharField(max_length=255, blank=True, null=True)
	is_active = models.BooleanField(default=True) #bisa login
	staff = models.BooleanField(default=False) #staff bukan superuser
	admin = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []


	def __str__(self):
		return self.email
