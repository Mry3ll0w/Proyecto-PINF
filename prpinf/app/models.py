from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
#Las clases deberan tener la primera letra en mayusculas para poder distinguir en caso de usar variables 

'''
class User(models.Model):
    nickname = models.CharField(max_length=12,primary_key = True)
    mail = models.CharField(max_length= 30,default="")
    password = models.CharField(max_length= 12)
    t1_punct = models.IntegerField(default=0)
    t2_punct = models.IntegerField(default=0)
    done_test = models.BooleanField(default=False)
    '''

    
class Post(models.Model):

    post_id = models.AutoField(primary_key=True)
    author  = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=1440) #280 * 4 (tamaño Twitter * 5)
    topic = models.CharField(max_length =30, default = 'general' )
    post_date = models.DateTimeField(default=timezone.now)
    
    def __lt__(self, Post ):#Overload del operador < para hacer el sort mediante list.sort()==> O( n* log n )
        return self.post_date < Post.post_date
    
    #topico (se ven todos), sort fecha last 

class Calificaciones(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    t1_punct = models.IntegerField(default = 0)#definir un maximo a posteriori
    t2_punct = models.IntegerField(default = 0)
    ts_punct1 = models.IntegerField(default = 0)
    ts_punct2 = models.IntegerField(default = 0) #definir maximo valor a 50

class Pregunta_Cuestionario(models.Model):
    id_pregunta = models.IntegerField(primary_key=True, default=0)
    id_cuestionario = models.IntegerField(default=0)
    invertida = models.IntegerField(default=0) #Esta variable la usaremos para saber si la puntuacion del cuestionario esta invertida
    respuesta = models.IntegerField(default=0)

class Poll(models.Model):
    value = models.CharField(max_length=20)

#Vamos a ampliar la clase user por defecto

from django.contrib.auth.models import User

#PARA REFERENCIAR ESTAS VARIABLES EN EL USER HACEMOS    user.calificaciones.t1_punct por ejemplo

'''
class Calificaciones(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    t1_punct = models.IntegerField(default=0)
    ts_punct1 = models.IntegerField(default=0)
    ts_punct2 = models.IntegerField(default=0)
    '''
