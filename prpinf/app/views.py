

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
from .models import Calificaciones
#from .forms import UserFormRegistro, UserFormLogin, LoginForm, CreatePollForm, RegisterUserForm
from django.db import connections
from django.forms import ValidationError

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.password_validation import validate_password

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail

import random


# Create your views here.

#-----------------------------------------------------REGISTRO--------------------------------------------------------------------------------------

def post_prueba(request):


    if request.method == 'POST':

            #Siempre que trabajemos con un formulario, tenemos que comprobar que sea valido, esto se hace con la instruccion form.is_vail()

            #Con esto nos aseguramos de que la primera vez que se acceda a la url no busque un formulario lleno

                #Ahora vamos a obtener la data limpia del form, [usamos form.cleaned_data.get]esto se puede hacer de muchas formas pero esta me parece la mas clara

        email = request.POST['mail']
        username = request.POST['nickname']
        password = request.POST['password']

        try:

            if validate_password(password) is None:

            #Esta tirando error de validacion si introducimos contraseñas malas, lo cual esta bien pero no queremos
            #que salga el debugger cuando la pagina este activada. La cosa es la siguiente, ¿como evitamos que salga
            # error de validacion para que nos salga la pagina de error de contraseña?

                new_user = User.objects.create_user(username = username, password = password, email = email)

                new_user.save()

                calificiones_usuario = Calificaciones(id_usuario = new_user.id)

                calificiones_usuario.save()

                messages.success(request, 'Se ha creado la cuenta')
                return redirect('http://127.0.0.1:8000/app/prueba_login/')

        except ValidationError == 'This password is too short. It must contain at least 8 characters.':#['This password is too short. It must contain at least 8 characters.']:

            context = {'password_mal':''}

            errors = {'corta': 'Contraseña insegura: Introduzca una contraseña mas larga',
            'larga': 'Contraseña insegura: Introduzca una contraseña mas larga',
            'numerica': 'Contraseña insegura: Introduzca una contraseña con letras',
            'comun': 'Contraseña insegura: Contraseña muy comun, introduzca una mas compleja'}

            context['password_mal'] = errors['corta']
            #context['password_mal'] = errors['larga']
            #context['password_mal'] = errors['numerica']
            #context['password_mal'] = errors['comun']

            return render(request, 'prueba_post.html', context)

    return render(request, 'prueba_post.html') 

#------------------------------------------------------LOGIN---------------------------------------------------------------------------------------

def login_prueba(request):

    if request.method == 'POST':

        #Hay que verificar que el formato es valido, sino no se puede usar el cleaned.data


         #Tambien se pueden obtener los datos con el request.POST, ambas formas son igualmente validas

        username = request.POST['nickname']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)

            return redirect('http://161.35.37.208:8000/app/home/')

        else:

            return redirect('http://161.35.37.208:8000/app/prueba_login/')

    return render(request, 'prueba_login.html') 
 
# --------------------------------------------------- PRUEBA_POLL -------------------------------------------------------------------------- #
def prueba_poll(request): #OJO este es un endpoint de prueba para hacer otro (NO ES EL DEFINITIVO)
    # if request.method == 'POST': #Comprobamos si el metodo es correcto

    #     input_data = request.POST['poll'] # hacemos el catch de los datos que nos llegan del html
    #     print(request.POST)

    if request.method == 'POST':

        poll1 = request.POST['poll1']
        poll2 = request.POST['poll2']
        res = []
        res += [poll1, poll2]
        print ("Prueba con dict")
        for i in res:
            print (i)
        print ("Una vez recibimos los datos los tratamos con los options y tal")
        suma = 0
        for i in res:
            if i == 'option1':
                suma+=1
            elif i == 'option2':
                suma+=2
            elif i == 'option3':
                suma+=3
            elif i == 'option4':
                suma+=4
        print("El numero de puntos es: ",suma)
        #Test para comprobar el tema de los intervalos 
        if 2 <= suma <= 4:
            print(" entre 2 y 4")
        elif 5 <= suma <= 8:
            print (" entre 5 y 8")

    return render(request, 'prueba_poll.html')

#------------------------------------------PRUEBA DE VALORES POR PANTALLA A HTML------------
def prueba_valor(request):

    if request.method == 'POST':

        #Creas un context con el nombre de lo que vayas a pedir

        #MIRA ESTO ROLDAN ASI TIENES QUE GUARDAR LOS CONSEJOS

        #Y SOLO RELLENARLOS DE ESTA FORMA context['consejo 2'] = cagaste SI EL RESULTADO ES MENOR O IGUAL A 2 

        context = {'consejo_1':'', 'consejo_2':'', 'consejo_3':''}

        aux = {'aux1':'Eres un trozo de mierda'}
        

        #Pides lo que haga falta

        a = request.POST['a']
        b = request.POST['b']


        #Llenas "resultado" de esta forma con lo que sea que quieras pasar al html 

        context['consejo_1'] = aux['aux1']

        #Rendereas un html que ensenye la solucion PERO AHORA PASANDOLE LA VARIABLE context

        #Okay, vamos a irnos al html prueba_valor_solucion para ver como lo ensenyamos

        return render(request, 'prueba_valor_solucion.html', context)

    return render(request, 'prueba_valor.html')


#------------------------------------PRUEBA DE ENVIO DE TOKEN INTRODUCIENDO CORREITO--------------------

def token_prueba(request):

    if request.method == 'POST':

        mail = request.POST['mail']

        token_verify = random.randint(100000, 900000)

        send_mail(token_verify, 'Verificacion de cuenta', mail)

        return redirect('http://161.35.37.208:8000/app/verify_prueba/')

    return render(request, 'token_prueba.html')

# def verify_prueba(request):

#     if request.method == 'POST':

#         token 

#     return render (request, 'verify_prueba.html')

def pruebaad(request):


    return render(request, 'pruebaad.html')
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------                    
# ---------------------------------------------------VIEWS FINALES------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------REGISTRO FINAL-------------------------------------------------------------------------------------------------

def registro(request):

    if request.method == 'POST':
    
            #Siempre que trabajemos con un formulario, tenemos que comprobar que sea valido, esto se hace con la instruccion form.is_vail()

            #Con esto nos aseguramos de que la primera vez que se acceda a la url no busque un formulario lleno

                #Ahora vamos a obtener la data limpia del form, [usamos form.cleaned_data.get]esto se puede hacer de muchas formas pero esta me parece la mas clara

        email = request.POST['mail']
        username = request.POST['nickname']
        password = request.POST['password']

        new_user = User.objects.create_user(username = username, password = password, email = '')

        new_user.save()

        calificiones_usuario = Calificaciones(id_usuario = new_user.id)

        calificiones_usuario.save()

        messages.success(request, 'Se ha creado la cuenta')
        return redirect('http://161.35.37.208:8000/app/index/')

    return render(request, 'registro.html')

#----------------------------------------------------LOGIN FINAL-----------------------------------------------------------------------------
def index(request):

    if request.method == 'POST':
    
        #Hay que verificar que el formato es valido, sino no se puede usar el cleaned.data


         #Tambien se pueden obtener los datos con el request.POST, ambas formas son igualmente validas

        username = request.POST['nickname']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)

            return redirect('http://161.35.37.208:8000/app/home/')

        else:

            return redirect('http://161.35.37.208:8000/app/index/')

    return render(request, 'index.html')

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
        res18 = request.POST['poll18']

        res = [] #Creamos un diccionario donde vamos a almacenar todas las respuestas
        res +=[res1]
        res +=[res2]
        res +=[res3]
        res +=[res4]
        res +=[res5]
        res +=[res6]
        res +=[res7]
        res +=[res8]
        res +=[res9]
        res +=[res10]
        res +=[res11]
        res +=[res12]
        res +=[res13]
        res +=[res14]
        res +=[res15]
        res +=[res16]
        res +=[res17]
        res +=[res18]
        
        total_puntos = 0 #Almacenara el total de puntos obtenidos

        for i in res: #Recorremos el dict para meter los ptos 
            
            if i == 'option1':

                total_puntos+=1

            elif i == 'option2':

                total_puntos+=2

            elif i == 'option3':

                total_puntos+=3

            elif i == 'option4':

                total_puntos+=4
        
        print("El numero de puntos es: ",total_puntos)
        #Una vez obtenidos los puntos le asignamos la valoracion requerida
        consejo = " " # Almacenara el consejo a insertar (para a posteriori pasarlo a la clase) 
        '''
        ------------PUNTUACIONES-----------------
        Si la puntuacion está entre 
        18-35 ---> "Mala autoestima.Te recomiendo ahondar profundamente en aumentar tu autoestima"
        36-47 ---> "Baja Autoestima"
        48-59 ---> "En camino a alcanzar una alta autoestima"
        60-72 ---> "Alta autoestima" 
        '''
        # Miramos en que intervalo esta y metemos el consejo correspondiente

        #REVISAR LAS COMPROBACIONES, NO DA LO QUE DEBERIA

        if total_puntos <=35 :

            consejo_final = {'respuesta':'Mala autoestima.Te recomiendo ahondar profundamente en aumentar tu autoestima'}

        elif 36 <= total_puntos <= 47: 

            consejo_final = {'respuesta':'Baja Autoestima'}

        elif 48 <= total_puntos <=59:

            consejo_final = {'respuesta':'En camino a alcanzar una alta autoestima'}

        elif 60 <= total_puntos <= 72:

            consejo_final = {'respuesta':'Alta autoestima'}

        
        context = {'consejo':''}

        context['consejo'] = consejo_final['respuesta']

        cal = Calificaciones.objects.get(id_usuario = request.user.id)

        cal.t1_punct = total_puntos

        cal.save()
        
        return render(request, 'test1_solucion.html', context)
        
        #FALTA INSERTAR EL CONSEJO + DONE TEST1 + PUNTUACION EN EL USER LOGEADO

        
       
    return render(request,'test1.html')
        
#---------------------------------------------------Test Satisfaccion -----------------------------------------------------------
def testsatisfaction(request):

    context = {'total_puntos': ''}

    if request.method == 'POST': #Comprobamos si el metodo es correcto
        
        #FALTA OBTENER EL USUARIO LOGEADO Y ACTUALIZAR LAS PUNTUACIONES DEL MISMO

        # hacemos el catch de los datos que nos llegan del html
        p20 = request.POST['poll20'] 
        p21 = request.POST['poll21']
        
        if p20 == 'option1':
            
            punt_1 = 1
        
        elif p20 == 'option2':
            
            punt_1 = 2
        
        elif p20 == 'option3':
            
            punt_1 = 3
        
        elif p20 == 'option4':
            
            punt_1 = 4

#Para        
        if p21 == 'option1':
            
            punt_2 = 1
        
        elif p21 == 'option2':
            
            punt_2 = 2
        
        elif p21 == 'option3':
            
            punt_2 = 3
        
        elif p21 == 'option4':
            
            punt_2 = 4


        cal = Calificaciones.objects.get(id_usuario = request.user.id)

        cal.ts_punct1 = punt_1 
        cal.ts_punct2 = punt_2

        cal.save()
        
        return redirect('http://161.35.37.208:8000/app/perfil/')      
   
       
    return render(request,'test_satisfaccion.html')

#----------------------------------------------- VIEWS SIMPLES ------------------------------------------------------------------------------



def home(request):

    #ASI SE OBTIENE EL USERNAME DEL TIO QUE HA ACCEDIDO A ESTA REQUEST

    username = request.user.username

    print (username)

    return render(request, 'home.html')

def foro(request):
    
    return render(request, 'foro.html')


def perfil(request):

    return render(request, 'perfil.html')

def test(request):

    username = request.user.username

    print (username)

    return render(request, 'test.html')








