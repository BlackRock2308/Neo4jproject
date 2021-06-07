from django.urls import path
from .views import *

urlpatterns = [
    path('',accueil,name='accueil'),
    path('to-register/',register,name='signUp'),
    path('to-login/',myLogin,name='log'),
    path('to-logout/',myLogout,name='tologout'),
    path('profil/',profile,name='urprofile'),
    
]