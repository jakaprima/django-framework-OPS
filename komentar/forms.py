from django import forms
from django.forms import ModelForm
from .models import Komentar

class KomentarForm(ModelForm):
	class Meta:
		model = Komentar
		fields = (
			'penulis_komentar', 
			'email',
			'isi_komentar'
		)
		widgets = {
			'penulis_komentar': forms.TextInput(attrs={'placeholder': 'Masukkan Nama Anda'}),
			'email': forms.EmailInput(attrs={'placeholder': 'Masukkan Email Anda'}),
			'isi_komentar': forms.TextInput(attrs={'placeholder': 'Isi Komentar Anda'})
		}

