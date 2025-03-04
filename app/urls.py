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
    path('xalq-talimi-bolimi/talim-muassasalari/<slug:slug>', talim_muassa, name='talim_muassa'),
    path('xalq-talimi-bolimi/mtm/' , maktabgacha_talim_tashkiloti, name='mtm'),
    path('xalq-talimi-bolimi/bolim-ish-kun-tartibi/' , bolim_ish_kun_tartibi, name='bolim-ish-kun-tartibi'),
    path('xalq-talimi-bolimi/bosh-ish-orinlari/' , bosh_ish_orinlari, name='bosh-ish-orinlari'),
    path('xalq-talimi-bolimi/bolim-manzili/' , bolim_manzili, name='bolim-manzili'),

    path('matbuot-xizmati/elonral/', elonlar, name= 'elonlar'),
    path('matbuot-xizmati/bolim-ish-rejasi/', bolim_ish_rejasi, name= 'bolim-ish-rejasi'),
    path('matbuot-xizmati/fotogalereya/', fotogalereya, name= 'fotogalereya'),
    path('matbuot-xizmati/fotogalereya/<slug:slug>', foto, name= 'foto'),
    path('matbuot-xizmati/maruzalar/', maruzalar, name= 'maruzalar'),
    path('matbuot-xizmati/matbuot-xizmati/', matbuot_xizmati, name= 'matbuot-xizmati'),
    path('matbuot-xizmati/tadbirlar-rejasi/', tadbirlar_rejasi, name= 'tadbirlar-rejasi'),
    path('matbuot-xizmati/videogalereya/', videogalereya, name= 'videogalereya'),
    path('matbuot-xizmati/videogalereya/<slug:slug>', video, name= 'video'),
    path('matbuot-xizmati/yangiliklar/', yangiliklar, name= 'yangiliklar'),

    path('faoliyat/besh-muhim-tashabbus/', besh_muhim_tashabbus, name='besh-muhim-tashabbus'),
    path('faoliyat/besh-muhim-tashabbus/<slug:slug>', besh_tashabbus, name='besh-tashabbus'),
    path('faoliyat/faoliyat/', faoliyat, name='faoliyat'),
    path('faoliyat/korrupsiyaga-qarshi-kurash/', korrupsiyaga_qarshi_kurash, name='korrupsiyaga-qarshi-kurash'),
    path('faoliyat/talimga-doir-terminlar/', talimga_doir_terminlar, name='talimga-doir-terminlar'),

    path('oquvchilarga/oquvchilarga/', oquvchilarga, name='oquvchilarga'),
    path('oquvchilarga/davlat-ramzlari/gerb', gerb, name='gerb'),
    path('oquvchilarga/davlat-ramzlari/bayrog', flag, name='flag'),
    path('oquvchilarga/davlat-ramzlari/madhiya', gimn, name='gimn'),
    path('oquvchilarga/davlat-ramzlari/', davlat_ramzlari, name='davlat-ramzlari'),
    path('oquvchilarga/imtihon-materiallari/', imtihon_materiallari, name='imtihon-materiallari'),
    path('oquvchilarga/yoqolgan-shahodatnomani-tiklash-uchun-ariza-berish', yoqolgan_shahodatnomani_tiklash_uchun_ariza_berish, name='yoqolgan-shahodatnomani-tiklash-uchun-ariza-berish'),

    path('oqituvchilarga/fanlar-boyicha-testlar/', fanlar_boyicha_testlar, name='fanlar-boyicha-testlar'),
    path('oqituvchilarga/fanlar-boyicha-testlar/<slug:slug>', fan_test, name='fan-test'),
    path('oqituvchilarga/davlat-dasturlari/', davlat_dasturlari, name='davlat-dasturlari'),
    path('oqituvchilarga/davlat-dastur/<slug:slug>', davlat_dastur, name='davlat_dastur'),
    path('oqituvchilarga/kasaba-uyishmasi/', kasaba_uyishmasi, name='kasaba-uyishmasi'),
    path('oqituvchilarga/oqituvchilarga/', oqituvchilarga, name='oqituvchilarga'),
    path('oqituvchilarga/dars-ishlanmalar/', dars_ishlanmalar, name='dars-ishlanmalar'),
    path('oqituvchilarga/dars-ishlanmalar/<slug:slug>', dars_ishlanma, name='dars-ishlanma'),
    path('oqituvchilarga/huquq-va-majburiyatlar/', huquq_va_majburiyatlar ),
    path('oqituvchilarga/oqituvchilar-malakasini-oshirish/', oqituvchilar_malakasini_oshirish, name='oqituvchilar-malakasini-oshirish' ),
    path('oqituvchilarga/oqituvchilar-malakasini-oshirish/<slug:slug>', malaka, name='malaka' ),

    path('ota-onalarga/ota-onalarga/', ota_onalarga),
    path('ota-onalarga/bolani-bogchaga-joylashtirish-uchun-ariza-berish/', bolani_bogchaga_joylashtirish_uchun_ariza_berish),
    path('ota-onalarga/bolalarni-bogchaga-qabul-navbatini-tekshirish/', bolalarni_bogchaga_qabul_navbatini_tekshirish),
    path('ota-onalarga/bogcha-tolovlari-togrisida-malumot/', bogcha_tolovlari_togrisida_malumot),    
    path('ota-onalarga/bolani-maktabning-birinchi-sinfiga-joylashtirishga-ariza-yuborish/', bolani_maktabning_birinchi_sinfiga_joylashtirishga_ariza_yuborish),
    path('ota-onalarga/maktabga-oquvchilarni-qabul-qilish/', maktabga_oquvchilarni_qabul_qilish),
    path('ota-onalarga/bolalarni-bir-maktabdan-boshqa-maktabga-kochirish-uchun-ariza-yuborish/', bolalarni_bir_maktabdan_boshqa_maktabga_kochirish_uchun_ariza_yuborish),
    path('ota-onalarga/xorijiy-fuqarolar-uchun-bolalarini-maktabga-joylashtirish/', xorijiy_fuqarolar_uchun_bolalarini_maktabga_joylashtirish),

    path('normativ-hujjatlar/normativ-hujjatlar/' , normativ_hujjatlar),
    path('normativ-hujjatlar/prezident-qaror-va-farmonlari/' , prezident_qaror_va_farmonlari),
    path('normativ-hujjatlar/maktabgacha-va-maktab-talim-vazirligi-hayat-qarorlari/' , maktabgacha_va_maktab_talim_vazirligi_hayat_qarorlari),
    path('normativ-hujjatlar/maktabgacha-va-maktab-talim-vazirligi-meyoriy-hujjatlari/' , maktabgacha_va_maktab_talim_vazirligi_meyoriy_hujjatlari),
    path('normativ-hujjatlar/yunusobod-tumani-maktabgacha-va-maktab-talimi-bolimining-meyoriy-hujjatlari/' , yunusobod_tumani_maktabgacha_va_maktab_talimi_bolimining_meyoriy_hujjatlari),

]


