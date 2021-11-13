from django.db import models

# Create your models here.
#Las clases deberan tener la primera letra en mayusculas para poder distinguir en caso de usar variables 
class User(models.Model):
    nickname = models.CharField(max_length=12,primary_key = True)
    mail = models.CharField(max_length= 30,default="")
    password = models.CharField(max_length= 12)
    t1_punct = models.IntegerField(default=0)
    t2_punct = models.IntegerField(default=0)
    done_test = models.BooleanField(default=False)

    
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    author  = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=1440) #280 * 5 (tamaño Twitter * 5)

class Cuestionario(models.Model):
    id_cuestionario = models.AutoField(primary_key=True)
    contenido = models.CharField(max_length = 2000)#definir un maximo a posteriori
    punctuation = models.IntegerField(default=0) #definir maximo valor a 50

class Pregunta_Cuestionario(models.Model):
    id_pregunta = models.IntegerField(primary_key=True)
    id_cuestionario = models.IntegerField(default=0)
    invertida = models.IntegerField(default=0) #Esta variable la usaremos para saber si la puntuacion del cuestionario esta invertida
    respuesta = models.IntegerField(default=0)