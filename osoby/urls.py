from django.urls import path

from . import views

app_name = 'osoby'
urlpatterns = [
    path('', views.index, name='index'),
    path('lista/', views.lista, name='lista'),
    path('loguj/', views.loguj_osobe, name='loguj-osobe'),
]
