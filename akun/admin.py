from django.contrib import admin

# untuk custom model
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# form
from .forms import FormMembuatAkun, FormMerubahAkun

# model
from .models import Akun, Kontak, AktivasiEmail
# from django.contrib.auth.models import User

# admin.site.unregister(User)
# admin.site.unregister(Group)
UserBaru = get_user_model()


class UserAdmin(BaseUserAdmin):
    # form untuk menambah dan merubah user instance
    form = FormMerubahAkun
    add_form = FormMembuatAkun

    # field ini digunakan untuk menampilkan user model.
    # ini mengcopy definisi dari base useradmin
    # referensi spesifik field pada auth.User.
    list_display = ('email', 'tanggal_lahir', 'is_active', 'is_admin')
    list_filter = ('is_admin', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('tanggal_lahir',)}),
        ('Permissions', {'fields': ('is_active',  'is_admin')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'tanggal_lahir', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

# sekarang register user admin baru
admin.site.register(Akun, UserAdmin)
# dan sejak tidak menggunakan django built-in permission kita hapus Group model dari admin
admin.site.unregister(Group)

class AktivasiEmailAdmin(admin.ModelAdmin):
    search_fields = ['email']
    class Meta:
        model = AktivasiEmail

admin.site.register(AktivasiEmail, AktivasiEmailAdmin)



admin.site.register(Kontak)
