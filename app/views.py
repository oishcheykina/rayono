from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import *

# MTM BO"LIMI
def home(request):
    boss = Boss.objects.first()
    posts = Post.objects.all().order_by('-created_at')  
    last_post = Post.objects.exclude(category__name="Elon").order_by('-created_at').first()
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')  # Получаем номер страницы из GET-параметра
    page_obj = paginator.get_page(page_number)
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    dic = {
        'boss': boss,
        'page_obj': page_obj,
        'yil_dasturi': yil_dasturi,
        'last_post': last_post,
        'photos': photos ,
        'videos': videos ,
    }
    return render(request, 'index.html', dic)

def more(request, slug):
    boss = Boss.objects.first()
    post = get_object_or_404(Post, slug=slug)
    viewed_news = request.session.get('viewed_news', [])
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]

    if slug not in viewed_news:
        post.views += 1
        post.save(update_fields=['views'])
        viewed_news.append(slug)
        request.session['viewed_news'] = viewed_news
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    dic = {
        'boss': boss,
        'post': post,
        'yil_dasturi': yil_dasturi,
        'photos': photos ,
        'videos': videos ,
    }
    return render(request, 'more.html', dic)
def xalq_talimi_bolimi(request):
    boss = Boss.objects.first()
    posts = Rahbar.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')  # Получаем номер страницы из GET-параметра
    page_obj = paginator.get_page(page_number)
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    dic = {
        'boss': boss,
        'page_obj': page_obj,
        'yil_dasturi': yil_dasturi,
        'photos': photos ,
        'videos': videos ,
    }
    return render(request , 'xalq-talimi-bolimi/xalq-talimi-bolimi.html', dic)

def rahbariyat(request):
    boss = Boss.objects.first()
    posts = Rahbar.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')  # Получаем номер страницы из GET-параметра
    page_obj = paginator.get_page(page_number)
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    dic = {
        'boss': boss,
        'page_obj': page_obj,
        'yil_dasturi': yil_dasturi,
        'photos': photos ,
        'videos': videos ,
    }
    return render(request, 'xalq-talimi-bolimi/rahbariyat.html', dic)

def apparat_xodimlari(request):
    boss = Boss.objects.first()
    posts = Apparat_Xodimi.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')  # Получаем номер страницы из GET-параметра
    page_obj = paginator.get_page(page_number)
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    dic = {
        'boss': boss,
        'page_obj': page_obj,
        'yil_dasturi': yil_dasturi,
        'photos': photos ,
        'videos': videos ,
    }
    return render(request , 'xalq-talimi-bolimi/apparat-xodimlari.html', dic)

def tarkibiy_tuzilma(request):
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    tarkibiy_tuzilma = Tarkibiy_Tuzilma.objects.first()
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    
    dic = {
        'boss': boss,
        'tarkibiy_tuzilma': tarkibiy_tuzilma,
        'yil_dasturi': yil_dasturi,
        'photos': photos ,
        'videos': videos ,
    }
    return render(request , 'xalq-talimi-bolimi/tarkibiy-tuzilma.html', dic)

def rahbariyat_qabul_kunlari(request):
    qabul_kunlari = Qabul_Kunlari.objects.all()
    qabul_kuni = Qabul_Kunlari.objects.first()
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    dic = {
        'boss': boss,
        'yil_dasturi': yil_dasturi,
        'qabul_kuni': qabul_kuni,
        'qabul_kunlari': qabul_kunlari,
        'photos': photos ,
        'videos': videos ,
    }
    return render(request , 'xalq-talimi-bolimi/rahbariyat-qabul-kunlari.html', dic)

def bolim_nizomi(request):
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    nizom = Qabul_Kunlari.objects.first()
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    dic = {
        'boss': boss,
        'yil_dasturi': yil_dasturi,
        'nizom': nizom,
        'photos': photos ,
        'videos': videos ,
    }
    return render(request , 'xalq-talimi-bolimi/bolim-nizomi.html', dic)

def talim_muassasalari(request):
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    direktorlar = Principals.objects.all()
    paginator = Paginator(direktorlar, 4)
    page_number = request.GET.get('page')  # Получаем номер страницы из GET-параметра
    page_obj = paginator.get_page(page_number)
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    dic = {
        'boss': boss,
        'yil_dasturi': yil_dasturi,
        'page_obj': page_obj,
        'photos': photos ,
        'videos': videos ,
    }
    return render(request , 'xalq-talimi-bolimi/talim-muassasalari.html', dic)

def talim_muassa(request, slug):
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    principal = get_object_or_404(Principals, slug=slug)
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    dic = {
        'boss': boss,
        'yil_dasturi': yil_dasturi,
        'principal': principal,
        'photos': photos ,
        'videos': videos ,
    }
    return render(request , 'xalq-talimi-bolimi/talim_muassa.html', dic)

def maktabgacha_talim_tashkiloti(request):
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    talim_tashkiloti = Talim_Tashkiloti.objects.first()
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    dic = {
        'boss': boss,
        'yil_dasturi': yil_dasturi,
        'talim_tashkiloti': talim_tashkiloti,
        'photos': photos ,
        'videos': videos ,
    }
    return render(request , 'xalq-talimi-bolimi/mtm.html', dic)

def bolim_ish_kun_tartibi(request):
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    kun_tartib_added = Kun_Tartibi.objects.first()
    kun_tartibi = Kun_Tartibi.objects.all()
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    dic ={
        'boss': boss,
        'yil_dasturi': yil_dasturi,
        'kun_tartib_added': kun_tartib_added,
        'kun_tartibi': kun_tartibi,
        'photos': photos ,
        'videos': videos ,
    }
    return render(request , 'xalq-talimi-bolimi/bolim-ish-kun-tartibi.html', dic)

def bosh_ish_orinlari(request):
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    bosh_ish_orinlar = Bosh_orinlar.objects.first()
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    dic = {
        'boss': boss,
        'yil_dasturi': yil_dasturi,
        'bosh_ish_orinlar': bosh_ish_orinlar,
        'photos': photos ,
        'videos': videos ,
    }
    return render(request , 'xalq-talimi-bolimi/bosh-ish-orinlari.html', dic)

def bolim_manzili(request):
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    manzil = Bolim_manzili.objects.first()
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    dic = {
    'boss': boss,
    'yil_dasturi': yil_dasturi,
    'manzil': manzil,
    'photos': photos ,
    'videos': videos ,
    }
    return render(request , 'xalq-talimi-bolimi/bolim-manzili.html', dic)

# O'QITUVCHILARGA

def oqituvchilarga(request):
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    dic = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos ,
        'videos': videos ,
    }      
    return render(request,'oqituvchilarga/oqituvchilarga.html' , dic )

def dars_ishlanmalar(request):
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    dars_ishlanmalar = Dars_Ishlanmalar.objects.all()
    paginator = Paginator(dars_ishlanmalar, 4)
    page_number = request.GET.get('page')  # Получаем номер страницы из GET-параметра
    page_obj = paginator.get_page(page_number)
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    dic = {
        'boss': boss,
        'yil_dasturi': yil_dasturi,
        'page_obj': page_obj,
        'photos': photos ,
        'videos': videos ,
    }
    return render(request,'oqituvchilarga/dars-ishlanmalar.html', dic )

def dars_ishlanma(request, slug):
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    dars_ishlanma = get_object_or_404(Dars_Ishlanmalar, slug=slug)
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    dic = {
        'boss': boss,
        'yil_dasturi': yil_dasturi,
        'dars_ishlanma': dars_ishlanma,
        'photos': photos ,
        'videos': videos ,
    }
    return render(request,'oqituvchilarga/dars-ishlanma.html', dic )

def fanlar_boyicha_testlar(request):
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    fan_testlar = Fan_Testlar.objects.all()
    paginator = Paginator(fan_testlar, 4)
    page_number = request.GET.get('page')  # Получаем номер страницы из GET-параметра
    page_obj = paginator.get_page(page_number)
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    dic = {
        'boss': boss,
        'yil_dasturi': yil_dasturi,
        'page_obj': page_obj,
        'photos': photos ,
        'videos': videos ,
    }
    return render(request,'oqituvchilarga/fanlar-boyicha-testlar.html', dic )

def fan_test(request, slug):
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    fan_test = get_object_or_404(Fan_Testlar, slug=slug)
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    dic = {
        'boss': boss,
        'yil_dasturi': yil_dasturi,
        'fan_test': fan_test,
        'photos': photos ,
        'videos': videos ,
    }
    return render(request,'oqituvchilarga/fan-test.html', dic )

def davlat_dasturlari(request):
    davlat_dasturlari = Davlat_Dasturlari.objects.all().order_by('-created_at')
    paginator = Paginator(davlat_dasturlari, 4)
    page_number = request.GET.get('page')  # Получаем номер страницы из GET-параметра
    page_obj = paginator.get_page(page_number)
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    dic = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos ,
        'videos': videos ,
        'page_obj': page_obj,
    }      
    return render(request,'oqituvchilarga/davlat-dasturlari.html', dic )

def davlat_dastur(request, slug):
    davlat_dastur = get_object_or_404(Davlat_Dasturlari, slug=slug)
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    dic = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos ,
        'videos': videos ,
        'davlat_dastur': davlat_dastur,
    }      
    return render(request,'oqituvchilarga/davlat-dastur.html', dic )

def kasaba_uyishmasi(request):
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    dic = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos ,
        'videos': videos ,
    }      
    return render(request,'oqituvchilarga/kasaba-uyishmasi.html', dic )

def huquq_va_majburiyatlar(request):
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    qonun = Talim_Qonun.objects.first()
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    dic = {
        'boss': boss,
        'yil_dasturi': yil_dasturi,
        'qonun': qonun,
        'photos': photos ,
        'videos': videos ,
    }
    return render(request,'oqituvchilarga/huquq-va-majburiyatlar.html', dic)

def oqituvchilar_malakasini_oshirish(request):
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    malaka_oshirish = Malaka_Oshirish.objects.all()
    last_malaka = Malaka_Oshirish.objects.order_by('-created_at').first()
    paginator = Paginator(malaka_oshirish, 4)
    page_number = request.GET.get('page')  # Получаем номер страницы из GET-параметра
    page_obj = paginator.get_page(page_number)
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    dic = {
        'boss': boss,
        'yil_dasturi': yil_dasturi,
        'page_obj': page_obj,
        'last_malaka': last_malaka,   
        'photos': photos ,
        'videos': videos ,  # Общее количество малакасов
    }
    return render(request,'oqituvchilarga/oqituvchilar-malakasini-oshirish.html', dic)

def malaka(request, slug):
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    malaka = get_object_or_404(Malaka_Oshirish, slug=slug)
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    dic = {
        'boss': boss,
        'yil_dasturi': yil_dasturi,
        'malaka': malaka,
        'photos': photos ,
        'videos': videos , 
    }
    return render(request,'oqituvchilarga/malaka-oshirish.html', dic)

#MATBUOT-XIMATI

def elonlar(request):
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    posts = Post.objects.filter(category__name="Elon").order_by('-created_at')  
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')  # Получаем номер страницы из GET-параметра
    page_obj = paginator.get_page(page_number)
    dic = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos ,
        'videos': videos ,
        'page_obj': page_obj,  # Объекты постов для текущей страницы
    }
    return render(request,'matbuot-xizmati/elonlar.html' ,dic)

def bolim_ish_rejasi(request):
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    dic = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos ,
        'videos': videos ,
    }
    return render(request,'matbuot-xizmati/bolim-ish-rejasi.html',dic )

def fotogalereya(request):
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    photo_main = Photo.objects.all().order_by('-created_at')
    paginator = Paginator(photo_main, 4)
    page_number = request.GET.get('page')  # Получаем номер страницы из GET-параметра
    page_obj = paginator.get_page(page_number)
    dic = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos ,
        'videos': videos ,
        'page_obj': page_obj,  # Объекты фотографий для текущей страницы
    }
    return render(request,'matbuot-xizmati/fotogalereya.html',dic )

def foto(request, slug):
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    photo = get_object_or_404(Photo, slug=slug)
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    dic = {
        'boss': boss,
        'yil_dasturi': yil_dasturi,
        'photo': photo,
        'photos': photos ,
        'videos': videos ,
    }
    return render(request,'matbuot-xizmati/foto.html', dic)

def maruzalar(request):
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    dic = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos ,
        'videos': videos ,
    }       
    return render(request,'matbuot-xizmati/maruzalar.html'  , dic)

def matbuot_xizmati(request):
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    dic = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos ,
        'videos': videos ,
    }       
    return render(request,'matbuot-xizmati/matbuot-xizmati.html' , dic )

def tadbirlar_rejasi(request):
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    dic = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos ,
        'videos': videos ,
    }       
    return render(request,'matbuot-xizmati/tadbirlar-rejasi.html' , dic )

def videogalereya(request):
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    videos_main = Video_Galereya.objects.all().order_by('-created_at')
    paginator = Paginator(videos_main, 4)
    page_number = request.GET.get('page')  # Получаем номер страницы из GET-параметра
    page_obj = paginator.get_page(page_number)
    dic = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos ,
        'videos': videos ,
        'page_obj': page_obj,  # Объекты видеографий для текущей страницы
    }       
    return render(request,'matbuot-xizmati/videogalereya.html' , dic )

def video(request, slug):
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    video = get_object_or_404(Video_Galereya, slug=slug)
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    dic = {
        'boss': boss,
        'yil_dasturi': yil_dasturi,
        'video': video,
        'photos': photos ,
        'videos': videos ,
    }
    return render(request,'matbuot-xizmati/video.html', dic )
def yangiliklar(request):
    boss = Boss.objects.first()
    posts = Post.objects.exclude(category__name="Elon").order_by('-created_at')  
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')  # Получаем номер страницы из GET-параметра
    page_obj = paginator.get_page(page_number)
    yil_dasturi = Yil_Dasturi.objects.first()
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    dic = {
        'boss': boss,
        'page_obj': page_obj,
        'yil_dasturi': yil_dasturi,
                'photos': photos ,
        'videos': videos ,
    }
    return render(request,'matbuot-xizmati/yangiliklar.html', dic )

#FAOLIYAT

def besh_muhim_tashabbus(request):
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    muhim_tashabbuslar = Besh_Tashshabus.objects.all().order_by('-created_at')
    paginator = Paginator(muhim_tashabbuslar, 4)
    page_number = request.GET.get('page')  # Получаем номер страницы из GET-параметра
    page_obj = paginator.get_page(page_number)
    dic = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos ,
        'videos': videos ,
        'page_obj': page_obj,  # Объекты для текущей страницы
    }      
    return render(request,'faoliyat/besh-muhim-tashabbus.html' , dic )

def besh_tashabbus(request, slug):
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    post = get_object_or_404(Besh_Tashshabus, slug=slug)
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    dic = {
        'boss': boss,
        'yil_dasturi': yil_dasturi,
        'post': post,
        'photos': photos ,
        'videos': videos ,
    }
    return render(request,'faoliyat/besh-tashabbus.html', dic )

def faoliyat(request):
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    dic = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos ,
        'videos': videos ,
    }      
    return render(request,'faoliyat/faoliyat.html' , dic )

def korrupsiyaga_qarshi_kurash(request):
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    korrupsiyaga_qarshi_kurash = Korrupsia_Qarshi.objects.all()
    paginator = Paginator(korrupsiyaga_qarshi_kurash, 4)
    page_number = request.GET.get('page')  # Получаем номер страницы из GET-параметра
    page_obj = paginator.get_page(page_number)
    dic = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos ,
        'videos': videos ,
        'page_obj': page_obj,  # Объекты для текущей страницы
    }      
    return render(request,'faoliyat/korrupsiyaga-qarshi-kurash.html' , dic )

def korrupsia(request, slug):
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    post = get_object_or_404(Korrupsia_Qarshi, slug=slug)
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    dic = {
        'boss': boss,
        'yil_dasturi': yil_dasturi,
        'post': post,
        'photos': photos ,
        'videos': videos ,
    }
    return render(request,'faoliyat/korrupsia.html', dic )

def talimga_doir_terminlar(request):
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    dic = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos ,
        'videos': videos ,
    }      
    return render(request,'faoliyat/talimga-doir-terminlar.html' , dic )

#OQUVCHILARGA

def oquvchilarga(request):
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    dic = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos ,
        'videos': videos ,
    }      
    return render(request,'oquvchilarga/oquvchilarga.html' , dic )

def davlat_ramzlari(request):
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    dic = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos ,
        'videos': videos ,
    }      
    return render(request,'oquvchilarga/davlat-ramzlari.html' , dic )

def gerb(request):
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    dic = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos ,
        'videos': videos ,
    }      
    return render(request,'oquvchilarga/gerb.html' , dic )

def gimn(request):
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    dic = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos ,
        'videos': videos ,
    }      
    return render(request,'oquvchilarga/gimn.html' , dic )

def flag(request):
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    dic = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos ,
        'videos': videos ,
    }      
    return render(request,'oquvchilarga/flag.html' , dic )

def imtihon_materiallari(request):
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    post = Imtihon_Materiallari.objects.order_by('-created_at').first()
    dic = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos ,
        'videos': videos ,
        'post': post,  # Для отображения первого поста в шаблоне
    }      
    return render(request,'oquvchilarga/imtihon-materiallari.html' , dic )

def yoqolgan_shahodatnomani_tiklash_uchun_ariza_berish(request):
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    post = Shahodatnomani_Tiklash.objects.order_by('-created_at').first()
    dic = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos ,
        'videos': videos ,
        'post': post,  # Для отображения первого поста в шаблоне
    }      
    return render(request,'oquvchilarga/yoqolgan-shahodatnomani-tiklash-uchun-ariza-berish.html' , dic )


#OTA-ONALARGA

def ota_onalarga(request):
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    dic = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos ,
        'videos': videos ,
    }      
    return render(request , 'ota-onalarga/ota-onalarga.html' , dic)

def bolani_bogchaga_joylashtirish_uchun_ariza_berish(request):
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    dic = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos ,
        'videos': videos ,
    }      
    return render(request , 'ota-onalarga/bolani-bogchaga-joylashtirish-uchun-ariza-berish.html' , dic)

def bolalarni_bogchaga_qabul_navbatini_tekshirish(request):
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    dic = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos ,
        'videos': videos ,
    }      
    return render(request , 'ota-onalarga/bolalarni-bogchaga-qabul-navbatini-tekshirish.html' , dic)

def bogcha_tolovlari_togrisida_malumot(request):
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    dic = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos ,
        'videos': videos ,
    }      
    return render(request , 'ota-onalarga/bogcha-tolovlari-togrisida-malumot.html' , dic)

def bolani_maktabning_birinchi_sinfiga_joylashtirishga_ariza_yuborish(request):
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    dic = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos ,
        'videos': videos ,
    }      
    return render(request , 'ota-onalarga/bolani-maktabning-birinchi-sinfiga-joylashtirishga-ariza-yuborish.html' , dic)

def maktabga_oquvchilarni_qabul_qilish(request):
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    dic = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos ,
        'videos': videos ,
    }      
    return render(request , 'ota-onalarga/maktabga-oquvchilarni-qabul-qilish.html ', dic)

def bolalarni_bir_maktabdan_boshqa_maktabga_kochirish_uchun_ariza_yuborish(request):
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    dic = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos ,
        'videos': videos ,
    }      
    return render(request , 'ota-onalarga/bolalarni-bir-maktabdan-boshqa-maktabga-kochirish-uchun-ariza-yuborish.html' , dic)

def xorijiy_fuqarolar_uchun_bolalarini_maktabga_joylashtirish(request):
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    dic = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos ,
        'videos': videos ,
    }      
    return render(request , 'ota-onalarga/xorijiy-fuqarolar-uchun-bolalarini-maktabga-joylashtirish.html' , dic)



# NORMATIV-HUJATLAR


def normativ_hujjatlar(request):
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    dic = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos ,
        'videos': videos ,
    }    
    return render(request , 'normativ-hujjatlar/normativ-hujjatlar.html' , dic)

def prezident_qaror_va_farmonlari(request):
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    prezident_qarorlari = Prezident_Qarorlari.objects.all().order_by('-created_at')  # Modeldan ma’lumotlarni olish

    context = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos,
        'videos': videos,
        'prezident_qarorlari': prezident_qarorlari,  # Template-ga uzatiladigan ma'lumot
    }

    return render(request, 'normativ-hujjatlar/prezident-qaror-va-farmonlari.html', context)


def maktabgacha_va_maktab_talim_vazirligi_hayat_qarorlari(request):

    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    hayat_qarorlari = Hayat_Qarorlari.objects.all().order_by('-created_at')  # Modeldan ma’lumotlarni olish

    context = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos,
        'videos': videos,
        'hayat_qarorlari': hayat_qarorlari,  # Template-ga uzatiladigan ma'lumot
    }

    return render(request, 'normativ-hujjatlar/maktabgacha-va-maktab-talim-vazirligi-hayat-qarorlari.html', context)

def maktabgacha_va_maktab_talim_vazirligi_meyoriy_hujjatlari(request):
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    meyoriy_hujjatlar = Meyoriy_Hujjatlar.objects.all().order_by('-created_at')  # Yangi model ma’lumotlarini olish

    context = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos,
        'videos': videos,
        'meyoriy_hujjatlar': meyoriy_hujjatlar,  # Template-ga uzatiladigan ma'lumot
    }

    return render(request, 'normativ-hujjatlar/maktabgacha-va-maktab-talim-vazirligi-meyoriy-hujjatlari.html', context)

def denov_tumani_maktabgacha_va_maktab_talimi_bolimining_meyoriy_hujjatlari(request):
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    tuman_hujjatlar = Tuman_Hujjatlari.objects.all()
    paginator = Paginator(tuman_hujjatlar, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos,
        'videos': videos,
        'page_obj': page_obj,
    }

    return render(request, 'normativ-hujjatlar/denov-tumani-maktabgacha-va-maktab-talimi-bolimining-meyoriy-hujjatlari.html', context)

def meyoriy_hujjat(request, slug):
    photos = Photo.objects.all().order_by('-created_at')[:4]
    videos = Video_Galereya.objects.all().order_by('-created_at')[:4]
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    post = get_object_or_404(Tuman_Hujjatlari, slug=slug)
    dic = {
        'yil_dasturi': yil_dasturi,
        'boss': boss,
        'photos': photos,
        'videos': videos,
        'post': post,
    }
    return render(request, 'normativ-hujjatlar/meyoriy-hujjat.html', dic)







