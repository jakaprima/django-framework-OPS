# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from komentar.models import Komentar
from kategori.models import Kategori
from akun.models import Penulis
from settingweb.models import SettingWeb
from artikel.models import Artikel
from akun.models import Kontak


# Register your models here.

# admin.site.register(models.Postlist)
admin.site.register(Komentar)
admin.site.register(Kategori)
admin.site.register(Penulis)
admin.site.register(SettingWeb)
admin.site.register(Artikel)
admin.site.register(Kontak)
