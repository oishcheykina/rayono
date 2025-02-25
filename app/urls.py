from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('more/<slug:slug>/', more, name='more'),
    path('xalq-talimi-bolimi/xalq-talimi-bolimi/' , xalq_talimi_bolimi, name='xalq-talimi-bolimi'),
    path('oqituvchilarga/oqituvchilarga/', oqituvchilarga, name='oqituvchilarga'),
    path('oqituvchilarga/dars-ishlanmalar/', dars_ishlanmalar, name='dars-ishlanmalar'),
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
    path('oqituvchilarga/fanlar-boyicha-testlar/', fanlar_boyicha_testlar, name='fanlar-boyicha-testlar'),
    path('oqituvchilarga/davlat-dasturlari/', davlat_dasturlari, name='davlat-dasturlari'),
    path('oqituvchilarga/kasaba-uyishmasi/', kasaba_uyishmasi, name='kasaba-uyishmasi'),
    path('matbuot-xizmati/elonral/', elonlar, name= 'elolar'),
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
]
