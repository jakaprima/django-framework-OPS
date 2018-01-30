from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# from django.views.generic.edit import FormView
from .forms import FormLogin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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
	"""docstring for ArtikelList"""
	# def __init__(self, arg):
	# 	super(ArtikelList, self).__init__()
	# 	self.arg = arg

class TambahPostView(TemplateView):
	template_name = 'adminapps/adm_dashboard/tambahpost.html'	

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

