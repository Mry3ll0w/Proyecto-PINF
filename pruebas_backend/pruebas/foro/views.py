from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User

#Se encarga de mostrar el foro
def foro(request):
    if request.method == 'GET':

        posts = Post.objects.all()#Metemos todas las querys de los post en la DB en post

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
            
            p = Post(author=User.objects.get(username=input['author']), content=input['content'])
        
            p.save()#Se guardan los datos y se redirige al home donde se ven los post
            
            return redirect('http://127.0.0.1:8000/foro/home')
            
    return render(request, 'create_post.html')
