from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def xalq_talimi_bolimi(request):
    return render(request , 'xalq-talimi-bolimi/xalq-talimi-bolimi.html')

def oqituvchilarga(request):
    return render(request,'oqituvchilarga/oqituvchilarga.html' )

def dars_ishlanmalar(request):
    return render(request,'oqituvchilarga/dars-ishlanmalar.html' )

def rahbariyat(request):
    return render(request, 'xalq-talimi-bolimi/rahbariyat.html')

def apparat_xodimlari(request):
    return render(request , 'xalq-talimi-bolimi/apparat-xodimlari.html')

def tarkibiy_tuzilma(request):
    return render(request , 'xalq-talimi-bolimi/tarkibiy-tuzilma.html')

def rahbariyat_qabul_kunlari(request):
    return render(request , 'xalq-talimi-bolimi/rahbariyat-qabul-kunlari.html')

def bolim_nizomi(request):
    return render(request , 'xalq-talimi-bolimi/bolim-nizomi.html')

