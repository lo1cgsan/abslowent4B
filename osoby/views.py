from django.http import HttpResponse
from django.shortcuts import render

from osoby.models import Klasa, Absolwent

def index(request):
    return HttpResponse("<h1>Witaj w Django!</h1>")

def lista(request):
    absolwenci = Absolwent.objects.all()
    kontekst = {'absolwenci': absolwenci}
    return render(request, 'osoby/lista_absolwentow.html', kontekst)
