from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ImproperlyConfigured
from django.views.generic import TemplateView, ListView, CreateView, edit
from django.http import HttpResponse
from django.contrib.auth import login as auth_login, authenticate

from django.contrib.auth.models import User
from .models import SettingWeb, Artikel, Komentar, Kategori, Kontak

from django.utils.text import slugify
from django.db import connection

from .forms import KomentarForm, DaftarForm, KontakForm
from django.core.urlresolvers import reverse_lazy, reverse
import requests

# Create your views here.
# class FormListView(edit.FormMixin, ListView):
# 	form_class = DaftarForm
# 	def get(self, request, *args, **kwargs):
# 	    # From ProcessFormMixin
# 	    form_class = self.get_form_class()
# 	    self.form = self.get_form(form_class)

# 	    # From BaseListView
# 	    self.object_list = self.get_queryset()
# 	    allow_empty = self.get_allow_empty()
# 	    if not allow_empty and len(self.object_list) == 0:
# 	        raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
# 	                      % {'class_name': self.__class__.__name__})

# 	    context = self.get_context_data(object_list=self.object_list, form=self.form)
# 	    return self.render_to_response(context)

# 	def post(self, request, *args, **kwargs):
# 	    return self.get(request, *args, **kwargs)
		




# class Index(FormListView):
# 	model = Artikel
# 	template_name = "homepage/index.html"
# 	def get_context_data(self, *args, **kwargs):
# 		context = super(Index, self).get_context_data(*args, **kwargs)
# 		return super(Index, self).render_to_response(context)

	





def kirim_email_aktivasi(data_email):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxcb7f24d03e004cd2878d280f2cfa5a55.mailgun.org/messages",
        auth=("api", "key-88fb3541b7b81461c15199fec9aa023e"),
        data=data_email)







# class Index(TemplateView):
# 	template_name = 'homepage/index.html'
# 	def get_context_data(self, *args, **kwargs):
# 		context = super(Index,self).get_context_data(*args, **kwargs)
# 		return context

# 	def get(self, request, *args, **kwargs):
# 	    context = super(Index, self).get_context_data(*args, **kwargs)
# 	    queryset = SettingWeb.objects.first()
# 	    queryset_artikel = Artikel.objects.all().order_by('-created_at')
# 	    context['data_setting_web'] = queryset
# 	    context['data_artikel'] = queryset_artikel
# 	    context['daftar_form'] = DaftarForm
# 	    return super(Index, self).render_to_response(context)

# 	def post(self, request, *args, **kwargs):
# 		form = DaftarForm(request.POST)
# 		if form.is_valid():
# 			# user = form.save()
# 			self.data_email = {
# 				"from": "Blog Jaka Prima <postmaster@sandboxcb7f24d03e004cd2878d280f2cfa5a55.mailgun.org>",
# 			    "to": [form.cleaned_data.get('first_name'), form.cleaned_data.get('email')],
# 			    "subject": 'aktivasi email',
# 			    "html": 'klik aktivasi disini <a href="#">halo</a>'
# 			}
# 			kirim_email_aktivasi(self.data_email)

# 			# username = form.cleaned_data.get('username')
# 			# password = form.cleaned_data.get('password')
# 			# userauthenticated = authenticate(username=username, password=password)
# 			# print userauthenticated
# 			# auth_login(request, userauthenticated)
# 			return redirect('homepage:index')
# 		elif form.is_invalid():
# 			return HttpResponse('halo')

# 		return render(request, 'homepage/index.html', {'daftar_form': DaftarForm()})

def Index(request):
	if request.method == 'POST':
		form = DaftarForm(request.POST)
		if form.is_valid():
			data_email = {
				"from": "Blog Jaka Prima <postmaster@sandboxcb7f24d03e004cd2878d280f2cfa5a55.mailgun.org>",
			    "to": [form.cleaned_data.get('first_name'), form.cleaned_data.get('email')],
			    "subject": 'aktivasi email',
			    "html": 'klik aktivasi disini <a href="#">halo</a>'
			}
			kirim_email_aktivasi(data_email)
			messages.info(request, 'aktivasi telah dikirim ke email')
			return redirect('homepage:index')
		else:
			messages.error(request, 'tidak berhasil')
	else:
		form = DaftarForm()

	queryset_setting_web = SettingWeb.objects.first()
	queryset_artikel = Artikel.objects.all().order_by('-created_at')
	context = {
		'data_setting_web': queryset_setting_web,
		'data_artikel': queryset_artikel,
		'daftar_form': form,
	}
	return render(request, 'homepage/index.html', context)



class Detail(TemplateView):
	form_class = KomentarForm()
	template_name = 'homepage/detail.html'

	def get(self, request, artikelslug=None, *args, **kwargs):
		context = super(Detail, self).get_context_data(**kwargs)
		a = artikelslug.replace('-', ' ')
		# queryset_artikel = get_object_or_404(Artikel, judul_artikel=a)
		# queryset_komentar = get_object_or_404(Komentar, artikel__judul_artikel=a)
		queryset_artikel = Artikel.objects.get(judul_artikel__contains=a)
		queryset_komentar = Komentar.objects.filter(artikel__judul_artikel__contains=a)

		form_class = KomentarForm()

		queryset = SettingWeb.objects.first()
		self.context = {
			'data_artikel': queryset_artikel,
			'data_setting_web': queryset,
			'data_komentar': queryset_komentar,
			'form_class': form_class,
		}
		return super(Detail, self).render_to_response(self.context)

	def post(self, request, artikelslug, *args, **kwargs):
		a = artikelslug.replace('-', ' ')
		queryset_artikel = get_object_or_404(Artikel, judul_artikel=a)

		form = KomentarForm(request.POST)
		if form.is_valid():
			komentar = form.save(commit=False)
			komentar.artikel = queryset_artikel
			komentar.penulis_komentar = request.user
			komentar.isi_komentar = request.POST.get('isi_komentar')
			komentar.save()

			monthstring =  "%02d" % (queryset_artikel.created_at.month,)

			return  redirect('homepage:url-detailartikel', 
				tahun=queryset_artikel.created_at.year, 
				bulan=(monthstring), 
				artikelslug=(artikelslug))
			# return reverse('homepage:url-detailartikel', kwargs={
			# 	'tahun'=2018,
			# 	'bulan'=%02,
			# 	'artikelslug'='f'
			# })
			# return reverse('homepage:url-detailartikel', args=[2018, 02, 'f'])
			# return super(Detail, self).get(*args, **kwargs);

		# instance = Komentar(artikel=queryset_artikel, penulis_komentar=request.user, isi_komentar=request.POST.get('isi_komentar'))
		# instance.save()


		# data_form_komentar = request.POST.get('isi_komentar')
		# form = KomentarForm(data_form_komentar)
		# form.save()

# class CreateKomentar(TemplateView):

class Coba(TemplateView):
	def get(self, request, **kwargs):
		return HttpResponse('halo')
	def post(self, request, **kwargs):
		return redirect('homepage:testing', data1=2018)

def keranjang(request):
	# print request.session 
	# apa aja yang bisa kita pakai
	# print dir(request.session) 
	# 'session_key', 'set_expiry'
	# request.session.set_expiry(300) # 5 menit
	# print request.session.session_key
	request.session['nama_depan'] = 'jaka session'

	return HttpResponse('halo')

# def tentangkami(request):
# 	kontak_form = KontakForm(request.POST or None)
# 	context = {
# 		"form": kontak_form,
# 	}

# 	if kontak_form.is_valid():
# 		print kontak_form.cleaned_data
# 	return render(request, 'tentang/index.html', context)

# class TentangKami(TemplateView):
# 	template_name = 'tentang/index.html'
# 	def get(self, request, *args, **kwargs):
# 		context = super(TentangKami, self).get_context_data(**kwargs)
# 		kontak_form = KontakForm(request.POST or None)
# 		context = {
# 			"form": kontak_form
# 		}
# 		return super(TentangKami, self).render_to_response(context)
# 	def post(self, request, *args, **kwargs):
# 		self.context = super(TentangKami, self).get_context_data(*args, **kwargs)
# 		kontak_form = KontakForm(request.POST or None)
# 		if kontak_form.is_valid():
# 			self.context.update({
# 				"form": kontak_form
# 			})
# 			print(kontak_form.cleaned_data)
# 			return super(TentangKami, self).render_to_response(self.context)

# 		self.context.update({
# 			"form": kontak_form
# 		})
# 		return super(TentangKami, self).render_to_response(self.context)

class TentangKami(CreateView):
	# form_class = KontakForm
	form_class = KontakForm
	template_name = 'tentang/index.html'
	# model = Kontak
	# fields = ('nama_lengkap', 'email', 'isi_pesan')

	def get_queryset(self):
	    """
	    return `QuerySet` yang akan digunakan untuk mencari object
	    catatan method ini memanggil secara default implementasi dari `get_object` dan dan ga akan jalan jika `get_object` overridden
	    """
	    return Kontak.objects.all()


	def get_context_data(self, **kwargs):
	    """
	    masukkan form ke context dict.
	    """
	    if 'form' not in kwargs:
	        kwargs['form'] = KontakForm
	    return super(TentangKami, self).get_context_data(**kwargs)

	def form_valid(self, form):
		self.object = form.save()
		# print form.cleaned_data
		return super(TentangKami, self).form_valid(form)
		# return form.cleaned_data

	def form_invalid(self, form):
		return self.render_to_response(self.get_context_data(form=form))

class Daftar(CreateView):
	template_name = 'homepage/index.html'
	form_class = DaftarForm
	model = User
	def form_valid(self, form):
		self.object = form.save()
		return super(Index, self).get(form)
		# print form.cleaned_data
	def form_invalid(self, form):
		return Index.as_view()(halo='halo')


		# return super(Index, self).get(form)




