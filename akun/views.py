from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from .models import Akun, AktivasiEmail
from .forms import FormMembuatAkun, LoginForm


def konfirmasi_akun(request, key=None):
	if request.method == 'GET':
		qs = AktivasiEmail.objects.filter(key__iexact=key)
		konfirmasi_qs = qs.aksikonfirmasi()
		if konfirmasi_qs.count() == 1:
			obj = konfirmasi_qs.first()
			obj.aktivasi_akun()
			messages.success(request, 'email anda berhasil diaktifasi silahkan login menggunakan akun anda')
			return redirect('akun:login')

		

def kirim_ulang_aktivasi(request):
	pass

def daftar(request):
	form_class = FormMembuatAkun(request.POST or None)
	if form_class.is_valid():
		form_class.simpan()

		messages.success(request, 'Akun Berhasil Dibuat silahkan Cek Email untuk konfirmasi')
		return redirect('akun:login')

	context = {
		'form': form_class,
	}
	return render(request, 'akun/daftar.html', context)

# tidak boleh pake login func
def akun_login(request):
	form_class = LoginForm(request.POST or None)
	if form_class.is_valid():
		email = form_class.cleaned_data.get('email')
		password = form_class.cleaned_data.get('password')
		qs = Akun.objects.filter(email=email)
		if qs.exists():
			# jika terdaftar cek aktivasi
			not_active = qs.filter(is_active=False)
			if not_active.exists():
				# jika belum aktivasi
				messages.error(request, 'anda belum aktivasi')
			user = authenticate(request, username=email, password=password)
			if user is not None:
			    login(request, user)
			    return redirect('jualbeli:index')
			else:
				messages.error(request, 'anda belum menjadi member kami')
				context = {
					'form': form_class,
				}
				return render(request, 'akun/login.html', context)




	context = {
		'form': form_class,
	}
	return render(request, 'akun/login.html', context)

def akun_logout(request):
	logout(request)
	return redirect('jualbeli:index')