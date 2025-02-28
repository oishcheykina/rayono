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
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    dic = {
        'boss': boss,
        'page_obj': page_obj,
        'yil_dasturi': yil_dasturi,
        'last_post': last_post,
    }
    return render(request, 'index.html', dic)

def more(request, slug):
    boss = Boss.objects.first()
    post = get_object_or_404(Post, slug=slug)
    viewed_news = request.session.get('viewed_news', [])

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
    }
    return render(request, 'more.html', dic)
def xalq_talimi_bolimi(request):
    boss = Boss.objects.first()
    posts = Rahbar.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')  # Получаем номер страницы из GET-параметра
    page_obj = paginator.get_page(page_number)
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    dic = {
        'boss': boss,
        'page_obj': page_obj,
        'yil_dasturi': yil_dasturi,
    }
    return render(request , 'xalq-talimi-bolimi/xalq-talimi-bolimi.html', dic)

def rahbariyat(request):
    boss = Boss.objects.first()
    posts = Rahbar.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')  # Получаем номер страницы из GET-параметра
    page_obj = paginator.get_page(page_number)
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    dic = {
        'boss': boss,
        'page_obj': page_obj,
        'yil_dasturi': yil_dasturi,
    }
    return render(request, 'xalq-talimi-bolimi/rahbariyat.html', dic)

def apparat_xodimlari(request):
    boss = Boss.objects.first()
    posts = Apparat_Xodimi.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')  # Получаем номер страницы из GET-параметра
    page_obj = paginator.get_page(page_number)
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    dic = {
        'boss': boss,
        'page_obj': page_obj,
        'yil_dasturi': yil_dasturi,
    }
    return render(request , 'xalq-talimi-bolimi/apparat-xodimlari.html', dic)

def tarkibiy_tuzilma(request):
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    tarkibiy_tuzilma = Tarkibiy_Tuzilma.objects.first()
    
    dic = {
        'boss': boss,
        'tarkibiy_tuzilma': tarkibiy_tuzilma,
        'yil_dasturi': yil_dasturi,
    }
    return render(request , 'xalq-talimi-bolimi/tarkibiy-tuzilma.html', dic)

def rahbariyat_qabul_kunlari(request):
    qabul_kunlari = Qabul_Kunlari.objects.all()
    qabul_kuni = Qabul_Kunlari.objects.first()
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    dic = {
        'boss': boss,
        'yil_dasturi': yil_dasturi,
        'qabul_kuni': qabul_kuni,
        'qabul_kunlari': qabul_kunlari,
    }
    return render(request , 'xalq-talimi-bolimi/rahbariyat-qabul-kunlari.html', dic)

def bolim_nizomi(request):
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    nizom = Qabul_Kunlari.objects.first()
    dic = {
        'boss': boss,
        'yil_dasturi': yil_dasturi,
        'nizom': nizom,
    }
    return render(request , 'xalq-talimi-bolimi/bolim-nizomi.html', dic)

def talim_muassasalari(request):
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    direktorlar = Principals.objects.all()
    paginator = Paginator(direktorlar, 4)
    page_number = request.GET.get('page')  # Получаем номер страницы из GET-параметра
    page_obj = paginator.get_page(page_number)
    dic = {
        'boss': boss,
        'yil_dasturi': yil_dasturi,
        'page_obj': page_obj,
    }
    return render(request , 'xalq-talimi-bolimi/talim-muassasalari.html', dic)

def talim_muassa(request, slug):
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    principal = get_object_or_404(Principals, slug=slug)
    dic = {
        'boss': boss,
        'yil_dasturi': yil_dasturi,
        'principal': principal,
    }
    return render(request , 'xalq-talimi-bolimi/talim_muassa.html', dic)

def maktabgacha_talim_tashkiloti(request):
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    talim_tashkiloti = Talim_Tashkiloti.objects.first()
    dic = {
        'boss': boss,
        'yil_dasturi': yil_dasturi,
        'talim_tashkiloti': talim_tashkiloti,
    }
    return render(request , 'xalq-talimi-bolimi/mtm.html', dic)

def bolim_ish_kun_tartibi(request):
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    kun_tartib_added = Kun_Tartibi.objects.first()
    kun_tartibi = Kun_Tartibi.objects.all()
    dic ={
        'boss': boss,
        'yil_dasturi': yil_dasturi,
        'kun_tartib_added': kun_tartib_added,
        'kun_tartibi': kun_tartibi,
    }
    return render(request , 'xalq-talimi-bolimi/bolim-ish-kun-tartibi.html', dic)

def bosh_ish_orinlari(request):
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    bosh_ish_orinlar = Bosh_orinlar.objects.first()
    dic = {
        'boss': boss,
        'yil_dasturi': yil_dasturi,
        'bosh_ish_orinlar': bosh_ish_orinlar,
    }
    return render(request , 'xalq-talimi-bolimi/bosh-ish-orinlari.html', dic)

def bolim_manzili(request):
    boss = Boss.objects.first()
    yil_dasturi = Yil_Dasturi.objects.order_by('-created_at').first()
    manzil = Bolim_manzili.objects.first()
    dic = {
        'boss': boss,
        'yil_dasturi': yil_dasturi,
       'manzil': manzil,
    }
    return render(request , 'xalq-talimi-bolimi/bolim-manzili.html', dic)

# O'QITUVCHILARGA

def oqituvchilarga(request):
    return render(request,'oqituvchilarga/oqituvchilarga.html' )

def dars_ishlanmalar(request):
    return render(request,'oqituvchilarga/dars-ishlanmalar.html' )

def fanlar_boyicha_testlar(request):
     return render(request,'oqituvchilarga/fanlar-boyicha-testlar.html' )

def davlat_dasturlari(request):
     return render(request,'oqituvchilarga/davlat-dasturlari.html' )

def kasaba_uyishmasi(request):
     return render(request,'oqituvchilarga/kasaba-uyishmasi.html' )

def huquq_va_majburiyatlar(request):
     return render(request,'oqituvchilarga/huquq-va-majburiyatlar.html' )

def oqituvchilar_malakasini_oshirish(request):
     return render(request,'oqituvchilarga/oqituvchilar-malakasini-oshirish.html' )


#MATBUOT-XIMATI

def elonlar(request):
     return render(request,'matbuot-xizmati/elonlar.html' )

def bolim_ish_rejasi(request):
     return render(request,'matbuot-xizmati/bolim-ish-rejasi.html' )

def fotogalereya(request):
     return render(request,'matbuot-xizmati/fotogalereya.html' )

def maruzalar(request):
     return render(request,'matbuot-xizmati/maruzalar.html' )

def matbuot_xizmati(request):
     return render(request,'matbuot-xizmati/matbuot-xizmati.html' )

def tadbirlar_rejasi(request):
     return render(request,'matbuot-xizmati/tadbirlar-rejasi.html' )

def videogalereya(request):
     return render(request,'matbuot-xizmati/videogalereya.html' )

def yangiliklar(request):
    boss = Boss.objects.first()
    posts = Post.objects.all().order_by('-created_at')  
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')  # Получаем номер страницы из GET-параметра
    page_obj = paginator.get_page(page_number)
    yil_dasturi = Yil_Dasturi.objects.first()
    dic = {
        'boss': boss,
        'page_obj': page_obj,
        'yil_dasturi': yil_dasturi,
    }
    return render(request,'matbuot-xizmati/yangiliklar.html', dic )

#FAOLIYAT

def besh_muhim_tashabbus(request):
     return render(request,'faoliyat/besh-muhim-tashabbus.html' )

def faoliyat(request):
     return render(request,'faoliyat/faoliyat.html' )

def korrupsiyaga_qarshi_kurash(request):
     return render(request,'faoliyat/korrupsiyaga-qarshi-kurash.html' )

def talimga_doir_terminlar(request):
     return render(request,'faoliyat/talimga-doir-terminlar.html' )

#OQUVCHILARGA

def oquvchilarga(request):
     return render(request,'oquvchilarga/oquvchilarga.html' )

def davlat_ramzlari(request):
     return render(request,'oquvchilarga/davlat-ramzlari.html' )

def imtihon_materiallari(request):
     return render(request,'oquvchilarga/imtihon-materiallari.html' )

def yoqolgan_shahodatnomani_tiklash_uchun_ariza_berish(request):
     return render(request,'oquvchilarga/yoqolgan-shahodatnomani-tiklash-uchun-ariza-berish.html' )


#OTA-ONALARGA

def ota_onalarga(request):
     return render(request , 'ota-onalarga/ota-onalarga.html')

def bolani_bogchaga_joylashtirish_uchun_ariza_berish(request):
     return render(request , 'ota-onalarga/bolani-bogchaga-joylashtirish-uchun-ariza-berish.html')

def bolalarni_bogchaga_qabul_navbatini_tekshirish(request):
     return render(request , 'ota-onalarga/bolalarni-bogchaga-qabul-navbatini-tekshirish.html')

def bogcha_tolovlari_togrisida_malumot(request):
     return render(request , 'ota-onalarga/bogcha-tolovlari-togrisida-malumot.html')

def bolani_maktabning_birinchi_sinfiga_joylashtirishga_ariza_yuborish(request):
     return render(request , 'ota-onalarga/bolani-maktabning-birinchi-sinfiga-joylashtirishga-ariza-yuborish.html')

def maktabga_oquvchilarni_qabul_qilish(request):
     return render(request , 'ota-onalarga/maktabga-oquvchilarni-qabul-qilish.html')

def bolalarni_bir_maktabdan_boshqa_maktabga_kochirish_uchun_ariza_yuborish(request):
     return render(request , 'ota-onalarga/bolalarni-bir-maktabdan-boshqa-maktabga-kochirish-uchun-ariza-yuborish.html')

def xorijiy_fuqarolar_uchun_bolalarini_maktabga_joylashtirish(request):
     return render(request , 'ota-onalarga/xorijiy-fuqarolar-uchun-bolalarini-maktabga-joylashtirish.html')



# NORMATIV-HUJATLAR


def normativ_hujjatlar(request):
     return render(request , 'normativ-hujjatlar/normativ-hujjatlar.html')

def prezident_qaror_va_farmonlari(request):
     return render(request , 'normativ-hujjatlar/prezident-qaror-va-farmonlari.html')

def maktabgacha_va_maktab_talim_vazirligi_hayat_qarorlari(request):
     return render(request , 'normativ-hujjatlar/maktabgacha-va-maktab-talim-vazirligi-hayat-qarorlari.html')

def maktabgacha_va_maktab_talim_vazirligi_meyoriy_hujjatlari(request):
     return render(request , 'normativ-hujjatlar/maktabgacha-va-maktab-talim-vazirligi-meyoriy-hujjatlari.html')

def yunusobod_tumani_maktabgacha_va_maktab_talimi_bolimining_meyoriy_hujjatlari(request):
     return render(request , 'normativ-hujjatlar/yunusobod-tumani-maktabgacha-va-maktab-talimi-bolimining-meyoriy-hujjatlari.html')
