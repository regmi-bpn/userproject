from django.contrib import admin
from django.urls import path, include
from home import views


urlpatterns = [
    path('',views.index, name='home'),
    path('home',views.home, name='home'),
    path('login',views.loginUser, name='login'),
    path('logout',views.logoutUser, name='logout'),
    path('contact',views.contact, name='contact'),
    path('about',views.about, name='about'),
]
