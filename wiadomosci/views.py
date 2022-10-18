from django.shortcuts import render
from wiadomosci.models import Wiadomosc
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from wiadomosci.forms import WiadomoscForm
from django.contrib.auth.decorators import login_required

def lista_wiadomosci(request):
    wiadomosci = Wiadomosc.objects.all()
    kontekst = {'wiadomosci': wiadomosci}
    return render(request, 'wiadomosci/lista_wiadomosci2.html', kontekst)

@login_required()
def dodaj_wiadomosc(request):
    if request.method == 'POST':
        form = WiadomoscForm(request.POST)
        if form.is_valid():
            w = Wiadomosc(tresc=form.cleaned_data['tresc'], autor=request.user, data_d=form.cleaned_data['data_d'])
            w.save()
            messages.success(request, "Dodano nową wiadomość!")
            return redirect(reverse('wiadomosci:lista'))
    else:
        form = WiadomoscForm()
    return render(request, 'wiadomosci/dodaj_wiadomosc1.html', {'form': form})
