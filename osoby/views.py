from django.http import HttpResponse
from django.shortcuts import render, redirect
from osoby.models import Klasa, Absolwent
from osoby.forms import UserLoginForm, UserCreateForm, UserEditForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required

def index(request):
    return HttpResponse("<h1>Witaj w Django!</h1>")

def lista(request):
    absolwenci = Absolwent.objects.all()
    kontekst = {'absolwenci': absolwenci}
    return render(request, 'osoby/lista_absolwentow.html', kontekst)

def loguj_osobe(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            nazwa = form.cleaned_data['nazwa']
            haslo = form.cleaned_data['haslo']
            user = authenticate(request, username=nazwa, password=haslo)
            if user is not None:
                login(request, user)
                messages.success(request, "Zostałeś zalogowany!")
                return redirect(reverse('osoby:lista'))
            else:
                messages.error(request, "Błędny login lub hasło!")
    else:
        form = UserLoginForm()
    kontekst = {'form': form}
    return render(request, 'osoby/loguj_osobe.html', kontekst)

def wyloguj_osobe(request):
    logout(request)
    messages.info(request, "Zostałeś wylogowany!")
    return redirect(reverse('osoby:lista'))

def rejestruj_osobe(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Utworzono konto! Możesz się zalogować!")
            return redirect(reverse('osoby:loguj-osobe'))
    else:
        form = UserCreateForm()
    return render(request, 'osoby/rejestruj_osobe1.html', {'form': form})

@login_required()
def edytuj_osobe(request):
    try:
        a = Absolwent.objects.filter(user=request.user).first()
    except Absolwent.DoesNotExist:
        a = 0
    print(a)
    if request.method == 'POST':
        form = UserEditForm(instance=request.user, data=request.POST)
        if form.is_valid():
            # print(form.cleaned_data['klasa'])
            if a:
                a.klasa = form.cleaned_data['klasa']
                a.save()
            else:
                a = Absolwent.objects.create(user=request.user, klasa=form.cleaned_data['klasa'])
            form.save()
            messages.success(request, "Zaktualizowano dane użytkownika!")
            return redirect(reverse('osoby:lista'))
    else:
        if a:
            a = a.klasa.id
        form = UserEditForm(instance=request.user, initial={'klasa':a})
    return render(request, 'osoby/edytuj_osobe1.html', {'form': form})