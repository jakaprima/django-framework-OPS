from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

# Create your models here.
class SettingWeb(models.Model):
	nama_web = models.CharField(max_length=35)
	deskripsi_web = models.CharField(max_length=60)
	def __str__(self):
		return self.nama_web

class Artikel(models.Model):
	judul_artikel = models.CharField(max_length=200)
	isi_artikel = models.TextField()
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
		return self.judul_artikel



class Penulis(models.Model):
	nama = models.CharField(max_length=200)
	email = models.EmailField()

	def __str__(self):
		return self.nama
