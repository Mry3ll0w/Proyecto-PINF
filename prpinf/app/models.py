from django.db import models

# Create your models here.
#Las clases deberan tener la primera letra en mayusculas para poder distinguir en caso de usar variables 
class User(models.Model):
    first_name = models.CharField(max_length= 30,primary_key=True)
    password = models.CharField(max_length= 12)
    done_test = models.BooleanField(default=False)
    
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    author  = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=1440) #280 * 5 (tamaño Twitter * 5)