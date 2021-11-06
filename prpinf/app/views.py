
from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .forms import UserForm
from django.db import connections


# Create your views here.
def post_prueba(request):
    form = UserForm()
    if request.method == 'POST':
        data = request.POST    
        
    context = {'form':form}
    print(data['mail'],"  ",data['password'])
    #insercion en la base de la buena data
    
    User.objects.create(mail= data['mail'],password=data['password'])


    

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

