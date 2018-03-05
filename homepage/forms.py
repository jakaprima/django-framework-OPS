from django import forms
from django.forms import ModelChoiceField
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Komentar, Kontak

# class KontakForm(forms.Form):
# 	nama_lengkap = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs = {
# 				"class": "form-control",
# 				"placeholder": "Masukkan Nama Lengkap"
# 			}
# 		)
# 	)

# 	email = forms.EmailField(
# 		widget = forms.EmailInput(
# 			attrs = {
# 				"class": "form-control",
# 				"placeholder": "Masukkan Email Anda"
# 			}
# 		)
# 	)

# 	isi_pesan = forms.CharField(
# 		widget = forms.TextInput(
# 			attrs = {
# 				"class": "form-control",
# 				"placeholder": "Isi Pesan"
# 			}
# 		)
# 	)

# 	def clean_nama_lengkap(self):
# 		nama_lengkap = self.cleaned_data.get('nama_lengkap')
# 		if not "jaka" in nama_lengkap:
# 			raise forms.ValidationError("namanya harus pake kata jaka")
# 		return nama_lengkap

class KontakForm(forms.ModelForm):
	class Meta:
		model = Kontak
		fields = ('nama_lengkap', 'email', 'isi_pesan')

	def clean_nama_lengkap(self):
		nama_lengkap = self.cleaned_data.get('nama_lengkap')
		if not "jaka" in nama_lengkap:
			raise forms.ValidationError('nama harus diisi')
		return nama_lengkap





class KomentarForm(forms.ModelForm):
    class Meta:
        model = Komentar
        fields = ('isi_komentar',)
    # def label_from_instance(self, obj):
    	# print obj
        # return "My Object #%i" % obj.id
    # def __init__(self, *args, **kwargs):
    # 	user = kwargs.pop('user','')

# class NewTopicForm(forms.ModelForm):
#     message = forms.CharField(
#         widget=forms.Textarea(
#             attrs={'rows': 5, 'placeholder': 'What is on your mind?'}
#         ),
#         max_length=4000,
#         help_text='The max length of the text is 4000.'
#     )

#     class Meta:
#         model = Topic
#         fields = ['subject', 'message']


class DaftarForm(UserCreationForm):
	email = forms.CharField(max_length=90, required=True, widget=forms.EmailInput())
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	# def clean_username(self):
	# 	username = self.cleaned_data.get('username')
	# 	if not "jaka" in username:
	# 		raise forms.ValidationError('harus jaka')
	# 	return username





# class SignUpForm(UserCreationForm):
#     email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')


class FormKomentar(forms.Form):
	isi_komentar = forms.CharField(required=True)

	# def __init__(self, *args, **kwargs):
	# 	super(FormCreatePost, self).__init__(*args, **kwargs)
	# 	self.fields['judul_artikel'].widget.attrs.update({
	# 			'class': 'form-widget', 'placeholder': 'Masukkan Judul Artikel'
	# 		})
	# 	self.fields['isi_artikel'].widget.attrs.update({
	# 		'class': 'form-widget', 'placeholder': 'Masukkan Isi Artikel'
	# 		})

# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

# class SignUpForm(UserCreationForm):
#     email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')