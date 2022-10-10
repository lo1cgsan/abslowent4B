from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Witaj w Django!</h1>")

def lista(request):
    return HttpResponse("<h1>Lista absolwentów!</h1>")
