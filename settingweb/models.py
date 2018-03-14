# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models import Count
from tinymce.models import HTMLField

from django.core.urlresolvers import reverse

# Create your models here.
class SettingWeb(models.Model):
	nama_web = models.CharField(max_length=25)
	deskripsi_web = models.CharField(max_length=60)
	def __str__(self):
		return self.nama_web