from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class Index(TemplateView):
	template_name = 'adminapps/index.html'

class LoginView(TemplateView):
	template_name = 'adminapps/adm_dashboard/login.html'