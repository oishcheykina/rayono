from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('xalq-talimi-bolimi/xalq-talimi-bolimi/' , xalq_talimi_bolimi ),

    

]

