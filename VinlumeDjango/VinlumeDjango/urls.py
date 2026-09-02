from django.contrib import admin
from django.urls import path, include
from vinlumeApp import views
from storeApp import views as store_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.inicio, name='inicio'),
    path('ahora/', views.ahora, name='ahora'),
    path('vinlumeApp/', include('vinlumeApp.urls')),
    path('second_home/', include('secondApp.urls')),
    path('storeApp/', store_views.store_lobby, name='store_lobby')
]

