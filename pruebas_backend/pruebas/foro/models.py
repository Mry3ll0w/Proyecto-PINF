from django.db import models
from django.utils import timezone # timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):

    post_id = models.AutoField(primary_key=True)
    author  = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=1440) #280 * 4 (tamaño Twitter * 5)
    topic = models.CharField(max_length =30, default = 'general' )
    post_date = models.DateTimeField(default=timezone.now)
    
    def __lt__(self, Post ):#Overload del operador < para hacer el sort mediante list.sort()==> O( n* log n )
        return self.post_date < Post.post_date
    
    #topico (se ven todos), sort fecha last 