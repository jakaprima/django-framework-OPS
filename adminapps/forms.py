from django import forms

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
	isi_artikel = forms.CharField()
	def __init__(self, *args, **kwargs):
		super(FormCreatePost, self).__init__(*args, **kwargs)
		self.fields['judul_artikel'].widget.attrs.update({
				'class': 'form-widget', 'placeholder': 'Masukkan Judul Artikel'
		})
		self.fields['isi_artikel'].widget.attrs.update({
			'class': 'form-widget', 'placeholder': 'Masukkan Isi Artikel'
	})
	