from django.db import models

# Create your models here.
#Las clases deberan tener la primera letra en mayusculas para poder distinguir en caso de usar variables 
class User(models.Model):
    first_name = models.EmailField
    password = models.CharField(max_length= 12)
    done_test = models.BooleanField(default=False)
    posts = [models.CharField(max_length = 1240 )] # a usar despues