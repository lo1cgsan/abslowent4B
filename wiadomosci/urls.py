from django.urls import path

from . import views

app_name = 'wiadomosci'
urlpatterns = [
   path('', views.lista_wiadomosci, name='lista'),
   path('dodaj/', views.dodaj_wiadomosc, name='dodaj'),
]
