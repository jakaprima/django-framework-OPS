from django.contrib import admin

# Register your models here.
from .models import User
from .models import Penulis
from .models import Kontak


admin.site.register(User)
admin.site.register(Penulis)
admin.site.register(Kontak)
