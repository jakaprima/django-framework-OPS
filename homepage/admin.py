from django.contrib import admin

from . import models
# Register your models here.

# admin.site.register(models.Postlist)
admin.site.register(models.Komentar)
admin.site.register(models.Kategori)
admin.site.register(models.Penulis)
admin.site.register(models.SettingWeb)
admin.site.register(models.Artikel)