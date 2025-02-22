from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('xalq-talimi-bolimi/xalq-talimi-bolimi/' , xalq_talimi_bolimi, name='xalq-talimi-bolimi'),
    path('oqituvchilarga/oqituvchilarga/', oqituvchilarga, name='oqituvchilarga'),
    path('oqituvchilarga/dars-ishlanmalar/', dars_ishlanmalar, name='dars-ishlanmalar')
    

]

