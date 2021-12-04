from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    author  = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=1440) #280 * 5 (tamaño Twitter * 5)