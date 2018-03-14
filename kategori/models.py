# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
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

# def pre_save_post_receiver(sender, instance, *args, **kwargs):
# 	if not instance.slug:
# 		instance.slug = create_slug(instance)
# 	#exe membuat slg
# 	pre_save.connect(pre_save_post_receiver, sender=Orang)






# class Postlist(models.Model):
# 	penulis_id = models.ForeignKey(User, null=True, blank=True)
# 	artikel_id = models.ForeignKey(Artikel, null=True, blank=True)
# 	komentar_id = models.ForeignKey(Komentar, null=True, blank=True)

# 	def __str__(self):
# 		return str(self.komentar_id) + str(self.artikel_id)






