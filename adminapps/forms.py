from django import forms
from tinymce.widgets import TinyMCE

class FormLogin(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	def __init__(self, *args, **kwargs):
		super(FormLogin, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({
				'class': 'form-widget', 'autocomplete': 'off'
		})
		self.fields['password'].widget.attrs.update({
			'class' : 'form-widget',
			'autocomplete' : 'off'
		})


class FormCreatePost(forms.Form):
	judul_artikel = forms.CharField()
	isi_artikel = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
	def __init__(self, *args, **kwargs):
		super(FormCreatePost, self).__init__(*args, **kwargs)
		self.fields['judul_artikel'].widget.attrs.update({
				'style': 'margin-bottom:20px;', 'class': 'form-widget pure-u-1-2', 'placeholder': 'Masukkan Judul Artikel'
		})
	
