from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

# Create your models here.
class Penulis(models.Model):
	nama = models.CharField(max_length=200)
	email = models.EmailField()

	def __str__(self):
		return self.nama
