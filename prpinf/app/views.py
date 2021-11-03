
from django.shortcuts import render
from django.http import HttpResponse

from .forms import UserForm

# Create your views here.


def post_prueba(request):
    form = UserForm()
    if request.method == 'POST':
        print(request.POST) 
        #user_input = {'form':form}
    return render(request, 'prueba_post.html', user_input)




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

