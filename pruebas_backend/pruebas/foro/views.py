from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from collections import Counter

#Se encarga de mostrar el foro
def foro(request):
    if request.method == 'GET':

        #posts = sorted(Post.objects.all(),reverse=True )#Metemos todas las querys de los post en la DB en post
        posts = Post.objects.all()#Catch de todas las querys de la DB
        
        #1) obtenemos todos los topics
        topics = []
        for i in posts:
            if i.topic not in topics:
                topics.append(i.topic)

        #2) Filtramos cada uno de los posts por topic
        #2.1 Creamos una lista de listas ==> lista[topic1[.....],topic2[...]]
        list_by_topic=list(zip(Counter(topics).keys(), Counter(topics).values()))

        for i in list_by_topic:
            print (i)


        return render(request,'foro.html',{'db':posts})#le pasamos la base de datos en el context para que la muestre
    
    else:
        #En caso de tener otro tipo de acceso que no sea el correspondiente se manda un 500 (forbidden operation)
        return HttpResponse(status=403)


#Crea un post para meterlo en la DB
def create_post(request):

    if request.method == 'POST':
        #Variables
        users = User.objects.all() 
        input = request.POST #guarda el contenido
        token = False

        #Primero buscaremos si ese usuario existe en la base de datos
        for i in users:
            
            if i.username == input['author']:
            
                print('El usuario existe')
            
                token = True


        #Comprobamos si se ha encontrado
        if token==False: #No se encuentra se redirige al home
            
            return redirect('http://127.0.0.1:8000/foro/create_post')

        else:#Se encuentra==> lo creo
            
            p = Post(author=User.objects.get(username=input['author']), content=input['content'], topic=input['topic'])
        
            p.save()#Se guardan los datos y se redirige al home donde se ven los post
            
            return redirect('http://127.0.0.1:8000/foro/home')
            
    return render(request, 'create_post.html')
