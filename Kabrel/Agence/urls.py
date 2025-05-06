
from django.urls import path,include
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('login',login,name='login'),
    path('register',register,name='register'),
    path('hotel',hotel,name='hotel'),
    path('fb',fb,name='fb'),
    path('ck',ck,name='ck'),
    path('compte',compte,name='compte'),

]
