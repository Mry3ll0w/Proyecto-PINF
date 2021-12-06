from django.urls import path
from . import views

urlpatterns = [
    
    path('home/',views.foro),
    path('create_post',views.create_post)
    
]