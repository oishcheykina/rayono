from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')



def xalq_talimi_bolimi(request):
    return render(request , 'xalq-talimi-bolimi/xalq-talimi-bolimi.html')


