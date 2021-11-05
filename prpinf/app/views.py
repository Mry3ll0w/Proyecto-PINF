
from django.shortcuts import render
from django.http import HttpResponse

from .forms import UserForm
from django.db import connections


# Create your views here.
def post_prueba(request):
    form = UserForm()
    if request.method == 'POST':
        data = request.POST    
    context = {'form':form}
    
    print(data['password'])
    

    return render(request, 'prueba_post.html',context)





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

