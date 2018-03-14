from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,  View, UpdateView, DeleteView
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
# from django.views.generic.edit import FormView
from .forms import FormLogin, FormCreatePost
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from artikel.models import Artikel
from kategori.models import Kategori
from komentar.models import Komentar

from django.db.models import Count
from django.utils.text import slugify
from django.utils import timezone

# Create your views here.

class Index(TemplateView):
	template_name = 'adminapps/index.html'
	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		self.context = super(Index, self).get_context_data(**kwargs)
		return super(Index, self).dispatch(request, *args, **kwargs)
	def post(self, request, *args, **kwargs):
		return HttpResponse(status=404)

	# def get(self, request, *args, **kwargs):
	# 	return HttpResponse(status=404)

class LoginView(TemplateView):
	template_name = 'adminapps/adm_dashboard/login.html'
	def dispatch(self, request, *args, **kwargs):
	    self.context = super(LoginView, self).get_context_data(**kwargs)
	    return super(LoginView, self).dispatch(request, *args, **kwargs)

	def get(self, request, *args, **kwargs):
	    form = FormLogin()
	    self.context['form'] = form
	    return super(LoginView, self).render_to_response(self.context)

	def post(self, request, *args, **kwargs):
		form = FormLogin(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)

			if user is None:
				return HttpResponse('none dikeluarin')
			else:
				login(request, user)
			return redirect("/admin-panel/")

			# return HttpResponse(user)
			# if user is not None:
			# 	login(request, user)
			# 	return HttpResponse('coba' + login(request, user))

class LogoutView(View):
	def get(self, request, *args, **kwargs):
		logout(request)
		return redirect('admin-panel:url-adm-login')



class TambahPostView(TemplateView):
	template_name = 'adminapps/adm_dashboard/tambahpost.html'
	# def get_context_data(self, **kwargs):
	#     context = super(ArtikelList, self).get_context_data(**kwargs)
	#     context['data_kategori'] = Kategori.objects.all()
	#     return context


	def dispatch(self, request, *args, **kwargs):
	    self.context = super(TambahPostView, self).get_context_data(**kwargs)
	    self.context['data_kategori'] = Kategori.objects.all()
	    return super(TambahPostView, self).dispatch(request, *args, **kwargs)

	def get(self, request, *args, **kwargs):
		form = FormCreatePost()
		self.context['form'] = form
		# data_artikel = Artikel.objects.all()
		return super(TambahPostView, self).render_to_response(self.context)
	def post(self, request, *args, **kwargs):
		list_kategori_input = request.POST.getlist('kategori_input')
		# print list_kategori_input[1]
		artikel_baru = Artikel(
			penulis=request.user, 
			judul_artikel=request.POST.get('judul_artikel').lower(), 
			isi_artikel=request.POST.get('isi_artikel'),
			publish_status=request.POST.get('status_artikel')
			)
		artikel_baru.save()
		for x in list_kategori_input:
			artikel_baru.kategori_artikel.add(x)
			artikel_baru.save()
		# for(list_kategori_input):
		# 	artikel_baru.kategori_artikel.add(x)
		# 	artikel_baru.save()

		# print request.user
		# form = FormCreatePost(request.POST)
		# if form.is_valid():
		# 	instance = Artikel(penulis=request.user, judul_artikel=request.POST.get('judul_artikel'), isi_artikel=request.POST.get('isi_artikel'))
		# 	instance.save()
		return redirect('/admin-panel/posts/')




