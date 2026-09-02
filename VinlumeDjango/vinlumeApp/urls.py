from django.contrib import admin
from django.urls import path
from secondApp import views

urlpatterns = [
    path('second_home/', views.second_home, name='second_home'),
    path('saludo/', views.saludo, name='saludo'),
]

