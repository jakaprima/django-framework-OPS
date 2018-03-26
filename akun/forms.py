from django import forms
from django.forms import ModelForm, ModelChoiceField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Kontak, Akun, AktivasiEmail
import requests
from django.contrib.auth.forms import ReadOnlyPasswordHashField

import requests


# class DaftarForm(ModelForm):
# 	password1 = forms.CharField(label="password", widget=forms.PasswordInput(attrs={
# 		'placeholder': 'masukkan password anda'
# 		}))
# 	password2 = forms.CharField(label='password konfirmasi', widget=forms.PasswordInput(attrs={
# 			'placeholder': 'ulangi password diatas'
# 		}))

# 	class Meta():
# 		model = Akun
# 		fields = (
# 			'nama_depan',
# 			'nama_belakang',
# 			'nama_lengkap',
# 			'email',
# 		)

# 	def __init__(self, *args, **kwargs):
# 		super(DaftarForm, self).__init__(*args, **kwargs)
# 		self.fields['nama_depan'].widget.attrs.update({
# 				'placeholder':'masukkan nama depan anda'
# 			})
# 		self.fields['nama_belakang'].widget.attrs.update({
# 				'placeholder': 'masukkan nama belakang anda'
# 			})
# 		self.fields['nama_lengkap'].widget.attrs.update({
# 				'placeholder': 'masukkan nama lengkap anda'
# 			})
# 		self.fields['email'].widget.attrs.update({
# 				'placeholder': 'masukkan email anda'
# 			})

# 	# validasi
# 	def clean_password2(self):
# 		password1 = self.cleaned_data.get('password1')
# 		password2 = self.cleaned_data.get('password2')
# 		if password1 and password2 and password1 != password2:
# 			raise forms.ValidationError("password tidak sama")
# 		return password2

# 	def kirim_aktivasi(self):
# 		print 'kirim_aktivasi', self.data_email
# 		return requests.post(
# 		    "https://api.mailgun.net/v3/sandboxcb7f24d03e004cd2878d280f2cfa5a55.mailgun.org/messages",
# 		    auth=("api", "key-88fb3541b7b81461c15199fec9aa023e"),
# 		    data=self.data_email)

# 	def simpan(self, commit=True):
# 		# simpan layanan password dalam hashed format
# 		# print self
# 		user = super(DaftarForm, self).save(commit=False)
# 		user.set_password(self.cleaned_data['password1'])
# 		user.is_active = False
# 		if commit:
# 			user.save()

# 			self.data_email = {
# 				"from": "Blog Jaka Prima <postmaster@sandboxcb7f24d03e004cd2878d280f2cfa5a55.mailgun.org>",
# 			    "to": [
# 		    		self.cleaned_data['nama_depan'], 
# 		    		self.cleaned_data['email']
# 			    ],
# 			    "subject": 'aktivasi email',
# 			    "html": 'klik aktivasi disini <a href="#">halo</a>'
# 			}

# 			self.kirim_aktivasi()
# 		return user

class LoginForm(ModelForm):
	class Meta():
		model = Akun
		fields = (
			'email',
			'password'
		)

	def clean(self):
		pass

class DateInput(forms.DateInput):
    input_type = 'date'

class FormMembuatAkun(ModelForm):
    """form untuk membuat user baru. termasuk semua required field, plus perulangan password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Akun
        fields = ('email', 'tanggal_lahir')
        widgets = {
        	'tanggal_lahir': DateInput(attrs={
        		'placeholder': 'masukkan tanggal lahir'
        	})
        }

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("password tidak sama")
        return password2


    # def kirim_aktivasi(self):
    #   return requests.post(
    #       "https://api.mailgun.net/v3/sandboxcb7f24d03e004cd2878d280f2cfa5a55.mailgun.org/messages",
    #       auth=("api", "key-88fb3541b7b81461c15199fec9aa023e"),
    #       data=self.data_email)


    def simpan(self, commit=True):
        # Save the layanan password dalam hashed format
        user = super(FormMembuatAkun, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = False
        if commit:
            
            self.data_email = {
              "from": "Blog Jaka Prima <postmaster@sandboxcb7f24d03e004cd2878d280f2cfa5a55.mailgun.org>",
              "to": [
                  'Pendaftar Django', 
                  self.cleaned_data['email']
              ],
              "subject": 'aktivasi email',
              "html": 'klik aktivasi disini <a href="#">halo</a>'
            }

            # buat AktivasiEmail via signal(di model)
            # signal tereksekusi setiap method save() terpanggil
            user.save()


            # self.kirim_aktivasi()
        return user

class FormMerubahAkun(forms.ModelForm):
    """form untuk update user. termasuk semua field dalam user, tetapi menempatkan password field dnengan admin password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Akun
        fields = ('email', 'password', 'tanggal_lahir', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class KontakForm(ModelForm):
	class Meta:
		model = Kontak
		fields = (
			'nama_lengkap',
			'email',
			'isi_pesan'
		)


