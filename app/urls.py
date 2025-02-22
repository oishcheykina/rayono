from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('xalq-talimi-bolimi/xalq-talimi-bolimi/' , xalq_talimi_bolimi, name='xalq-talimi-bolimi'),
    path('oqituvchilarga/oqituvchilarga/', oqituvchilarga, name='oqituvchilarga'),
    path('oqituvchilarga/dars-ishlanmalar/', dars_ishlanmalar, name='dars-ishlanmalar'),
    path('xalq-talimi-bolimi/rahbariyat/' , rahbariyat),
    path('xalq-talimi-bolimi/apparat-xodimlari/' , apparat_xodimlari ),
    path('xalq-talimi-bolimi/tarkibiy-tuzilma/' , tarkibiy_tuzilma),
    path('xalq-talimi-bolimi/rahbariyat-qabul-kunlari/' , rahbariyat_qabul_kunlari),
    path('xalq-talimi-bolimi/bolim-nizomi/' , bolim_nizomi),
    
]
