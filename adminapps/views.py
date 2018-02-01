from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# from django.views.generic.edit import FormView
from .forms import FormLogin, FormCreatePost
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from homepage.models import Artikel, Kategori, Komentar
from django.db.models import Count

# Create your views here.

class Index(TemplateView):
	template_name = 'adminapps/base.html'
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
		return redirect('url-adm-login')

class ArtikelList(TemplateView):
	template_name = 'adminapps/adm_dashboard/semuapost.html'
	def get_context_data(self, **kwargs):
	    context = super(ArtikelList, self).get_context_data(**kwargs)
	    queryset = Artikel.objects.select_related().annotate(komentar_count=Count('komentar'))

	    # print queryset[0].komentar_count
	    # print queryset.query
	    # "homepage_artikel"."id",
	    # "homepage_artikel"."penulis_id",
	    # "homepage_artikel"."judul_artikel",
	    # "homepage_artikel"."kategori_artikel_id",
	    # "homepage_artikel"."isi_artikel",
	    # COUNT("homepage_komentar"."id") AS "komentar_count" FROM "homepage_artikel" LEFT OUTER JOIN "homepage_komentar" ON ( "homepage_artikel"."id" = "homepage_komentar"."artikel_id" ) GROUP BY "homepage_artikel"."id", "homepage_artikel"."penulis_id", "homepage_artikel"."judul_artikel", "homepage_artikel"."kategori_artikel_id", "homepage_artikel"."isi_artikel"

	    context = {
	    	'data_artikel': queryset,
	    }
	    return context

class TambahPostView(TemplateView):
	template_name = 'adminapps/adm_dashboard/tambahpost.html'

	# def get_context_data(self, **kwargs):
	#     context = super(TambahPostView, self).get_context_data(**kwargs)
	#     context['data_artikel'] = Artikel.objects.all()
	#     return context

	def dispatch(self, request, *args, **kwargs):
	    self.context = super(TambahPostView, self).get_context_data(**kwargs)
	    return super(TambahPostView, self).dispatch(request, *args, **kwargs)
	def get(self, request, *args, **kwargs):
		form = FormCreatePost()
		self.context['form'] = form
		# data_artikel = Artikel.objects.all()
		return super(TambahPostView, self).render_to_response(self.context)
	def post(self, request, *args, **kwargs):
		# print request.user
		form = FormCreatePost(request.POST)
		if form.is_valid():
			instance = Artikel(penulis=request.user, judul_artikel=request.POST.get('judul_artikel'), isi_artikel=request.POST.get('isi_artikel'))
			instance.save()
			return redirect('/admin-panel/posts/')




# class DashboardView(BaseAuthenticatedView):
	# template_name = 'adminapps/adm_dashboard/index.html'
	# context = {
	# 	'title': 'halo title'
	# }

	# def post(self, request, *args, **kwargs):
	#     return HttpResponse(status=404)

	# def get(self, request, *args, **kwargs):
	#     # page content
	#     title = "Data Statistics"
	#     message = request.session.get("message", None)
	#     self.context.update({
	#     	'': title
	#     })

	#     return super(DashboardView, self).render_to_response(self.context)

