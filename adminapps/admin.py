# from django.contrib import admin
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import Group
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .models import Pengguna

# User = get_user_model()

# class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    # form = UserAdminChangeForm
    # add_form = UserAdminCreationForm

    # field ini digunakan untuk displaying User Model.
    # ini menimpa definisi dari base UserAdmin
    # spesifik reference field pada auth.User.
    # list_display = ('email', 'admin')
    # list_filter = ('admin', 'staff', 'is_active')
    # fieldsets = (
    #     (None, {'fields': ('nama_lengkap', 'email', 'password')}),
    #    # ('Full name', {'fields': ()}),
    #     ('Permissions', {'fields': ('admin', 'staff', 'is_active',)}),
    # )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'password1', 'password2')}
    #     ),
    # )
    # search_fields = ('email', 'nama_lengkap',)
    # ordering = ('email',)
    # filter_horizontal = ()


# Register your models here.
# admin.site.unregister(User)
# admin.site.register(User)
