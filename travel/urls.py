from typing import ValuesView
from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('contact/',views.contact, name='contact'),
    path('ticket/',views.ticket, name='ticket'),
    path('registerPage/',views.registerPage, name='registerPage'),
    path('loginPage/',views.loginPage, name='loginPage'),
    path('logout/',views.logoutUser, name='logout'),
    path('test/',views.test, name='test'),
    path('home/',views.home, name='home'),
]
