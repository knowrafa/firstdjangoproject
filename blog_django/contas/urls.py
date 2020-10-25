from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.paginaInicial),
    path('login/', views.login),
    path('checkout/', views.checkout),
    #path('home/', views.paginaInicial()),
]