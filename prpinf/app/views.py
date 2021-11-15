

#
#    |  __ \|  ____/ ____| |        /\    / ____| |  __ \|  ____| | |        /\     |  _ \| |  | |  ____| \ | |   /\     |  __ \|  __ \ / __ \ / ____|  __ \     /\   |  \/  |   /\   / ____|_   _/ __ \| \ | |
#    | |__) | |__ | |  __| |       /  \  | (___   | |  | | |__    | |       /  \    | |_) | |  | | |__  |  \| |  /  \    | |__) | |__) | |  | | |  __| |__) |   /  \  | \  / |  /  \ | |      | || |  | |  \| |
#    |  _  /|  __|| | |_ | |      / /\ \  \___ \  | |  | |  __|   | |      / /\ \   |  _ <| |  | |  __| | . ` | / /\ \   |  ___/|  _  /| |  | | | |_ |  _  /   / /\ \ | |\/| | / /\ \| |      | || |  | | . ` |
#    | | \ \| |___| |__| | |____ / ____ \ ____) | | |__| | |____  | |____ / ____ \  | |_) | |__| | |____| |\  |/ ____ \  | |    | | \ \| |__| | |__| | | \ \  / ____ \| |  | |/ ____ \ |____ _| || |__| | |\  |
#    |_|  \_\______\_____|______/_/    \_\_____/  |_____/|______| |______/_/    \_\ |____/ \____/|______|_| \_/_/    \_\ |_|    |_|  \_\\____/ \_____|_|  \_\/_/    \_\_|  |_/_/    \_\_____|_____\____/|_| \_|
#
#
#                    1.-Si usas un comando nuevo, comentalo y explica que hace.
#                    2.-Espacia bien entre lineas de codigo que hagan diferentes cosas, esto nos resultara en un codigo mas limpio.
#                    3.-Ten claros los bucles que creas, donde empiezan y donde acaban.
#                    4.-Nos fijamos SIEMPRE en la documentacion oficial.
#                    5.-Si, y solo si, no entiendes el error lo buscas en stack overflow, teniendo siempre en cuenta la regla numero 1.
#                    6.-No reinventes la rueda, Django hace casi todo por ti, informate que seguro que lo que quieres hacer, django lo hace ya.
#                    7.-Si algo da error o no hace lo que quieres lo pones en un comentario para los demas programadores.





from django.db.models.query_utils import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from .forms import UserFormRegistro, UserFormLogin, LoginForm, CreatePollForm, RegisterUserForm
from django.db import connections
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required


# Create your views here.

#-----------------------------------------------------REGISTRO--------------------------------------------------------------------------------------

def post_prueba(request):

    if request.user.is_authenticated:

        return redirect('http://127.0.0.1:8000/app/prueba_login/')

    else:

        form = UserFormRegistro()

        if request.method == 'POST':

            form = UserFormRegistro(request.POST)
            context = {'form':form}

            #Siempre que trabajemos con un formulario, tenemos que comprobar que sea valido, esto se hace con la instruccion form.is_vail()

            #Con esto nos aseguramos de que la primera vez que se acceda a la url no busque un formulario lleno

            if form.is_valid():

                #Ahora vamos a obtener la data limpia del form, [usamos form.cleaned_data.get]esto se puede hacer de muchas formas pero esta me parece la mas clara

                mail = form.cleaned_data.get('mail')
                nickname = form.cleaned_data.get('nickname')
                password = form.cleaned_data.get('password')

                new_user = User(nickname = nickname, mail = mail, password = password, t1_punct = 0, t2_punct = 0, done_test= False)
                new_user.save()

                messages.success(request, 'Se ha creado la cuenta')
                return redirect('http://127.0.0.1:8000/app/prueba_login/')

        context = {'form':form}
        return render(request, 'prueba_post.html', context) 

#------------------------------------------------------LOGIN---------------------------------------------------------------------------------------

def login_prueba(request):

    if request.user.is_authenticated:

        return redirect('http://127.0.0.1:8000/app/home/')

    form = UserFormLogin()

    if request.method == 'POST':

        form = LoginForm(request.POST)
        context = {'form':form}

        #Hay que verificar que el formato es valido, sino no se puede usar el cleaned.data

        if form.is_valid():

            #Tambien se pueden obtener los datos con el request.POST, ambas formas son igualmente validas

            post_nickname = request.POST['nickname']
            post_password = request.POST['password']

            querys = User.objects.all()
            isRegistered = False

            #Vale a ver, django puede hacer el login por la cara, pero eso da una especie de permisos que no nos vienen al cuento
            #   asi que para nuestro login simplente verificaremos si el usuario esta en la base de datos y obviamente que sea la
            #   misma password.

            for i in querys:

                if i.nickname == post_nickname and i.password == post_password:

                        isRegistered = True

            if isRegistered == True:

                return redirect('http://127.0.0.1:8000/app/home/')

            else:
                return redirect('http://127.0.0.1:8000/prueba_login/')

    context = {'form':form}
    return render(request, 'prueba_login.html', context) 

# --------------------------------------------------- PRUEBA_POLL -------------------------------------------------------------------------- #
def prueba_poll(request): #OJO este es un endpoint de prueba para hacer otro (NO ES EL DEFINITIVO)
    if request.method == 'POST': #Comprobamos si el metodo es correcto

        input_data = request.POST['poll'] # hacemos el catch de los datos que nos llegan del html
        data2 = request.POST['poll2'] 
        #Comprobamos que lo recibido sea X y trabajamos con el , en este caso solo printeamos
        if input_data == 'option1':
            print (input_data)

        elif input_data == 'option2':
            print (input_data)

        elif input_data == 'option3':
            print (input_data)

        elif input_data == 'option4': 
            print (input_data)

        else:
            return HttpResponse(400, 'Invalid form') # En caso de no contener un JSON correcto obtendremos un 400 

    return render(request, 'prueba_poll.html')

<<<<<<< Updated upstream
# --------------------------------------------------- POLL_PARSER -------------------------------------------------------------------------- #
def test(request): #Endpoint para la redireccion de los test
    return render(request, 'test.html')
#----------------------------------------------------POLL -------------------------------------------------
def test1(request):
    if request.method == 'POST': #Comprobamos si el metodo es correcto
        
        #FALTA OBTENER EL USUARIO LOGEADO Y ACTUALIZAR LAS PUNTUACIONES DEL MISMO

        # hacemos el catch de los datos que nos llegan del html
        res1 = request.POST['poll1'] 
        res2 = request.POST['poll2'] 
        res3 = request.POST['poll3'] 
        res4 = request.POST['poll4'] 
        res5 = request.POST['poll5'] 
        res6 = request.POST['poll6'] 
        res7 = request.POST['poll7'] 
        res8 = request.POST['poll8'] 
        res9 = request.POST['poll9'] 
        res10 = request.POST['poll10'] 
        res11 = request.POST['poll11'] 
        res12 = request.POST['poll12'] 
        res13 = request.POST['poll13'] 
        res14 = request.POST['poll14']
        res15 = request.POST['poll15']
        res16 = request.POST['poll16']
        res17 = request.POST['poll17'] 
        res = []
        res +=res1+ res2+ res3+ res4+ res5+ res6
        #ahora recorremos los distintos
        
       


    return render(request,'test1.html')
=======

#----------------------------------------------------REGISTRO FINAL-------------------------------------------------------------------------------------------------

def registro(request):

    if request.method == 'POST':

        mail = request.POST['mail']
        nickname = request.POST['nickname']
        password = request.POST['password']

        print(mail)
        print(nickname)
        print(password)

    return render(request, 'registro.html') 


>>>>>>> Stashed changes
#-----------------------------------------------Views por implementar------------------------------------------------------------------------------



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




