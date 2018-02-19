from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth import login as auth_login, authenticate

from .models import SettingWeb, Artikel, Komentar, Kategori

from django.utils.text import slugify
from django.db import connection

from .forms import KomentarForm, DaftarForm
from django.core.urlresolvers import reverse_lazy, reverse
import requests
# Create your views here.

def kirim_email_aktivasi(data_email):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxcb7f24d03e004cd2878d280f2cfa5a55.mailgun.org/messages",
        auth=("api", "key-88fb3541b7b81461c15199fec9aa023e"),
        data=data_email)

class Index(TemplateView):
	template_name = 'homepage/index.html'
	def get(self, request, *args, **kwargs):
	    context = super(Index, self).get_context_data(**kwargs)
	    queryset = SettingWeb.objects.first()
	    queryset_artikel = Artikel.objects.all().order_by('-created_at')
	    # print request.session.get('nama_depan')
	    # queryset_kategori = Artikel.kategori_set.all()
	    # queryset = Artikel.objects.select_related().annotate(komentar_count=Count('komentar'))
	    # queryset_kategori = Kategori.Artikel_set.all()

	    # print queryset_artikel[1].kategori_artikel.all()

	    context['data_setting_web'] = queryset
	    context['data_artikel'] = queryset_artikel
	    context['daftar_form'] = DaftarForm
	    return super(Index, self).render_to_response(context)

	def post(self, request, *args, **kwargs):
		form = DaftarForm(request.POST)
		if form.is_valid():
			# user = form.save()
			self.data_email = {
				"from": "Blog Jaka Prima <postmaster@sandboxcb7f24d03e004cd2878d280f2cfa5a55.mailgun.org>",
			    "to": [form.cleaned_data.get('first_name'), form.cleaned_data.get('email')],
			    "subject": 'aktivasi email',
			    "html": 'klik aktivasi disini <a href="#">halo</a>'
			}


			kirim_email_aktivasi(self.data_email)

			

			# username = form.cleaned_data.get('username')
			# password = form.cleaned_data.get('password')
			# userauthenticated = authenticate(username=username, password=password)
			# print userauthenticated
			# auth_login(request, userauthenticated)
			return redirect('homepage:index')
		else:
			messages.error(request, 'tidak berhasil dibuat')
		return render(request, 'homepage/index.html', {'daftar_form': DaftarForm()})





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


