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