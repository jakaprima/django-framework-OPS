# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from core.models import TimeStampedModel

# Create your models here.

class Flavor(TimeStampedModel):
	judul = models.CharField(max_length=200)
