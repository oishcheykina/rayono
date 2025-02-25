from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import *

# MTM BO"LIMI
def home(request):
    boss = Boss.objects.first()
    posts = Post.objects.all().order_by('-created_at')  
    last_post = Post.objects.order_by('-created_at').first()
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')  # Получаем номер страницы из GET-параметра
    page_obj = paginator.get_page(page_number)
    yil_dasturi = Yil_Dasturi.objects.first()
    dic = {
        'boss': boss,
        'page_obj': page_obj,
        'yil_dasturi': yil_dasturi,
        'last_post': last_post,
    }
    return render(request, 'index.html', dic)

def more(request, slug):
    boss = Boss.objects.all()
    post = get_object_or_404(Post, slug=slug)
    viewed_news = request.session.get('viewed_news', [])

    if slug not in viewed_news:
        post.views += 1
        post.save(update_fields=['views'])
        viewed_news.append(slug)
        request.session['viewed_news'] = viewed_news
    yil_dasturi = Yil_Dasturi.objects.first()
    dic = {
        'boss': boss,
        'post': post,
        'yil_dasturi': yil_dasturi,
    }
    return render(request, 'more.html', dic)


def xalq_talimi_bolimi(request):
    return render(request , 'xalq-talimi-bolimi/xalq-talimi-bolimi.html')

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

def talim_muassasalari(request):
    return render(request , 'xalq-talimi-bolimi/talim-muassasalari.html')

def maktabgacha_talim_tashkiloti(request):
    return render(request , 'xalq-talimi-bolimi/mtm.html')

def bolim_ish_kun_tartibi(request):
        return render(request , 'xalq-talimi-bolimi/bolim-ish-kun-tartibi.html')

def bosh_ish_orinlari(request):
        return render(request , 'xalq-talimi-bolimi/bosh-ish-orinlari.html')

def bolim_manzili(request):
        return render(request , 'xalq-talimi-bolimi/bolim-manzili.html')


# O'QITUVCHILARGA
def oqituvchilarga(request):
    return render(request,'oqituvchilarga/oqituvchilarga.html' )

def dars_ishlanmalar(request):
    return render(request,'oqituvchilarga/dars-ishlanmalar.html' )
