from django.db import models

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
