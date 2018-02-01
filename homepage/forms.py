from django import forms
from django.forms import ModelChoiceField
from django.forms import ModelForm
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

    

class FormKomentar(forms.Form):
	isi_komentar = forms.CharField()
	def __init__(self, *args, **kwargs):
		super(FormCreatePost, self).__init__(*args, **kwargs)
		self.fields['judul_artikel'].widget.attrs.update({
				'class': 'form-widget', 'placeholder': 'Masukkan Judul Artikel'
		})
		self.fields['isi_artikel'].widget.attrs.update({
			'class': 'form-widget', 'placeholder': 'Masukkan Isi Artikel'
	})