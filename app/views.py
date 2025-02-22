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

