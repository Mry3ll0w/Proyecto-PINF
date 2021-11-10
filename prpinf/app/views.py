
from django.db.models.query_utils import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from .forms import UserForm
from django.db import connections
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required


# Create your views here.
'''
def post_prueba(request):
    form = UserForm()
    #if request.method == 'POST':
        #print(request.POST)        
    context = {'form':form}
    querys = User.objects.all()
    token = False
    for i in querys:
        if i.mail == request.POST.get('mail','') and i.password == request.POST.get('password',''):
            token = True

    if token == True: #creamos el user y tal
        print('································user y pass correcta ···········································333')
    else:
        print('·······················User o contraseña incorrecta····························')
    return render(request, 'prueba_post.html',context)
'''
#-------------------------ESTE REGISTROFUNCIONA DE LOCOS--------------------
#COSAS A TENER EN CUENTA:
#django comprueba de forma automatica al guardar en la base de datos si ya existe un user con ese nickname

def post_prueba(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = UserForm()
        if request.method == 'POST':
            form = UserForm(request.POST)
            context = {'form':form}
            if form.is_valid():
                #form.save()
                mail = form.cleaned_data.get('mail')
                nickname = form.cleaned_data.get('nickname')
                password = form.cleaned_data.get('password')
                new_user = User(nickname = nickname, mail = mail, password = password, t1_punct = 0, t2_punct = 0, done_test= False)
                new_user.save()
                messages.success(request, 'Se ha creado la cuenta')
                return redirect('http://127.0.0.1:8000/app/prueba_login/')

        context = {'form':form}
        return render(request, 'prueba_post.html', context) 

def login_prueba(request):

    form = UserForm();


    context = {'form':form}
    return render(request, 'prueba_login.html', context) 


def login(request):
    
    form = UserForm()
    #if request.method == 'POST':
        #print(request.POST)        
    context = {'form':form}
    querys = User.objects.all()
    token = False
    for i in querys:
        if i.mail == request.POST.get('mail','') and i.nickname == request.POST.get('nickname',' '):
            token = True

    if token == False: #creamos el user y tal
        insertion = User(mail = request.POST.get('mail',''),nickname='' ,password = request.POST.get('password',''),t1_punct=0,t2_punct=0,done_test=False)
        insertion.save()
    return render(request, 'login.html',context)


def registro(request):#codigo sin su html y tal
    form = UserForm()
    #if request.method == 'POST':
        #print(request.POST)        
    context = {'form':form}
    querys = User.objects.all()
    token = False
    for i in querys:
        if i.mail == request.POST.get('mail','') and i.nickname == request.POST.get('nickname',' '):
            token = True

    if token == False: #creamos el user y tal
        insertion = User(mail = request.POST.get('mail',''),nickname='' ,password = request.POST.get('password',''),t1_punct=0,t2_punct=0,done_test=False)
        insertion.save()

    return render(request, 'registro.html',context)


def home(request):
    return render(request, 'home.html')

def foro(request):
    return render(request, 'foro.html')

def index(request):
    return render(request, 'index.html')

def perfil(request):
    return render(request, 'perfil.html')


def test(request):
    return render(request, 'test.html')

