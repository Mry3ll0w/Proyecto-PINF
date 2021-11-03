from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def si(request):
    return render(request,'si.html',{'name':'tu madre L0L'})

def home(request):
    return render(request, 'home.html')

def foro(request):
    return render(request, 'foro.html')

def index(request):
    return render(request, 'index.html')

def perfil(request):
    return render(request, 'perfil.html')

def registro(request):
    return render(request, 'registro.html')

def test(request):
    return render(request, 'test.html')
