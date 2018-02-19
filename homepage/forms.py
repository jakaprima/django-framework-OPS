from django import forms
from django.forms import ModelChoiceField
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Komentar

class KomentarForm(forms.ModelForm):
    class Meta:
        model = Komentar
        fields = ('isi_komentar',)
    def label_from_instance(self, obj):
    	print obj
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