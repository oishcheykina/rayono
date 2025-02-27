from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('more/<slug:slug>/', more, name='more'),
    path('xalq-talimi-bolimi/xalq-talimi-bolimi/' , xalq_talimi_bolimi, name='xalq-talimi-bolimi'),
    path('xalq-talimi-bolimi/rahbariyat/' , rahbariyat, name='rahbariyat'),
    path('xalq-talimi-bolimi/apparat-xodimlari/' , apparat_xodimlari, name='apparat-xodimlari' ),
    path('xalq-talimi-bolimi/tarkibiy-tuzilma/' , tarkibiy_tuzilma, name='tarkibiy-tuzilma'),
    path('xalq-talimi-bolimi/rahbariyat-qabul-kunlari/' , rahbariyat_qabul_kunlari, name='rahbariyat-qabul-kunlari'),
    path('xalq-talimi-bolimi/bolim-nizomi/' , bolim_nizomi, name='bolim-nizomi'),
    path('xalq-talimi-bolimi/talim-muassasalari/' ,talim_muassasalari, name='talim-muassasalari'),
    path('xalq-talimi-bolimi/mtm/' , maktabgacha_talim_tashkiloti, name='mtm'),
    path('xalq-talimi-bolimi/bolim-ish-kun-tartibi/' , bolim_ish_kun_tartibi, name='bolim-ish-kun-tartibi'),
    path('xalq-talimi-bolimi/bosh-ish-orinlari/' , bosh_ish_orinlari, name='bosh-ish-orinlari'),
    path('xalq-talimi-bolimi/bolim-manzili/' , bolim_manzili, name='bolim-manzili'),

    path('matbuot-xizmati/elonral/', elonlar, name= 'elonlar'),
    path('matbuot-xizmati/bolim-ish-rejasi/', bolim_ish_rejasi, name= 'bolim-ish-rejasi'),
    path('matbuot-xizmati/fotogalereya/', fotogalereya, name= 'fotogalereya'),
    path('matbuot-xizmati/maruzalar/', maruzalar, name= 'maruzalar'),
    path('matbuot-xizmati/matbuot-xizmati/', matbuot_xizmati, name= 'matbuot-xizmati'),
    path('matbuot-xizmati/tadbirlar-rejasi/', tadbirlar_rejasi, name= 'tadbirlar-rejasi'),
    path('matbuot-xizmati/videogalereya/', videogalereya, name= 'videogalereya'),
    path('matbuot-xizmati/yangiliklar/', yangiliklar, name= 'yangiliklar'),

    path('faoliyat/besh-muhim-tashabbus/', besh_muhim_tashabbus, name='besh-muhim-tashabbus'),
    path('faoliyat/faoliyat/', faoliyat, name='faoliyat'),
    path('faoliyat/korrupsiyaga-qarshi-kurash/', korrupsiyaga_qarshi_kurash, name='korrupsiyaga-qarshi-kurash'),
    path('faoliyat/talimga-doir-terminlar/', talimga_doir_terminlar, name='talimga-doir-terminlar'),

    path('oquvchilarga/oquvchilarga/', oquvchilarga, name='oquvchilarga'),
    path('oquvchilarga/davlat-ramzlari/', davlat_ramzlari, name='davlat-ramzlari'),
    path('oquvchilarga/imtihon-materiallari/', imtihon_materiallari, name='imtihon-materiallari'),
    path('oquvchilarga/yoqolgan-shahodatnomani-tiklash-uchun-ariza-berish', yoqolgan_shahodatnomani_tiklash_uchun_ariza_berish, name='yoqolgan-shahodatnomani-tiklash-uchun-ariza-berish'),

    path('oqituvchilarga/fanlar-boyicha-testlar/', fanlar_boyicha_testlar, name='fanlar-boyicha-testlar'),
    path('oqituvchilarga/davlat-dasturlari/', davlat_dasturlari, name='davlat-dasturlari'),
    path('oqituvchilarga/kasaba-uyishmasi/', kasaba_uyishmasi, name='kasaba-uyishmasi'),
    path('oqituvchilarga/oqituvchilarga/', oqituvchilarga, name='oqituvchilarga'),
    path('oqituvchilarga/dars-ishlanmalar/', dars_ishlanmalar, name='dars-ishlanmalar'),
    path('oqituvchilarga/huquq-va-majburiyatlar/', huquq_va_majburiyatlar ),
    path('oqituvchilarga/oqituvchilar-malakasini-oshirish/', oqituvchilar_malakasini_oshirish ),

    path('ota-onalarga/ota-onalarga/', ota_onalarga),
    path('ota-onalarga/bolani-bogchaga-joylashtirish-uchun-ariza-berish/', bolani_bogchaga_joylashtirish_uchun_ariza_berish),
    path('ota-onalarga/bolalarni-bogchaga-qabul-navbatini-tekshirish/', bolalarni_bogchaga_qabul_navbatini_tekshirish),
    path('ota-onalarga/bogcha-tolovlari-togrisida-malumot/', bogcha_tolovlari_togrisida_malumot),    
    path('ota-onalarga/bolani-maktabning-birinchi-sinfiga-joylashtirishga-ariza-yuborish/', bolani_maktabning_birinchi_sinfiga_joylashtirishga_ariza_yuborish),
    path('ota-onalarga/maktabga-oquvchilarni-qabul-qilish/', maktabga_oquvchilarni_qabul_qilish),
    path('ota-onalarga/bolalarni-bir-maktabdan-boshqa-maktabga-kochirish-uchun-ariza-yuborish/', bolalarni_bir_maktabdan_boshqa_maktabga_kochirish_uchun_ariza_yuborish),
    path('ota-onalarga/xorijiy-fuqarolar-uchun-bolalarini-maktabga-joylashtirish/', xorijiy_fuqarolar_uchun_bolalarini_maktabga_joylashtirish),
]


