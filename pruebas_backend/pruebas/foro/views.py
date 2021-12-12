from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User


#Se encarga de mostrar el foro
def foro(request):
    if request.method == 'GET':

        
        posts = Post.objects.all()#Catch de todas las querys de la DB
        parser_list = []
        final_list = []
        #1) obtenemos todos los topics
        topics = []
        for i in posts:
            if i.topic not in topics:
                topics.append(i.topic)

        #2) Filtramos cada uno de los posts por topic
        for i in topics:          
            #Los ordenamos por fecha y los metemos en la lista temporal
            final_list.append(sorted(Post.objects.filter(topic=i),reverse=True))
            #para obtener multiples querys se usa el filter, el sorted los ordena con la sobrecarga de la fecha
            #reverse indica que  se ordena de mas antiguo a mas nuevo

        


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
