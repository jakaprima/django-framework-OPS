from django import forms
from django.forms import ModelForm, ModelChoiceField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Kontak

class DaftarForm(UserCreationForm):
	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2'
		)

class KontakForm(ModelForm):
	class Meta:
		model = Kontak
		fields = (
			'nama_lengkap',
			'email',
			'isi_pesan'
		)


