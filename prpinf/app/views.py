
from django.db.models.query_utils import Q
from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .forms import UserForm
from django.db import connections


# Create your views here.
def post_prueba(request):
    form = UserForm()
    #if request.method == 'POST':
        #print(request.POST)        
    context = {'form':form}
    querys = User.objects.all()
    token = False
    for i in querys:
        if i.mail == request.POST.get('mail',''):
            token = True

    if token == False: #creamos el user y tal
        insertion = User(mail = request.POST.get('mail',''),nickname='' ,password = request.POST.get('password',''),t1_punct=0,t2_punct=0,done_test=False)
        insertion.save()

    return render(request, 'prueba_post.html',context)

def login(request):
    form = UserForm()
    #if request.method == 'POST':
        #print(request.POST)        
    context = {'form':form}
    querys = User.objects.all()
    token = False
    for i in querys:
        if i.mail == request.POST.get('mail',''):
            token = True

    if token == True: #creamos el user y tal
        print('user encontrado')#rellenar con return de datos a html
    return render(request, 'login.html',context)


def registro(request):#codigo sin su html y tal
    form = UserForm()
    #if request.method == 'POST':
        #print(request.POST)        
    context = {'form':form}
    querys = User.objects.all()
    token = False
    for i in querys:
        if i.mail == request.POST.get('mail',''):
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

