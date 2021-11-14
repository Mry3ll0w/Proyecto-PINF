from django.urls import path
from . import views

urlpatterns = [
    
    path('home/', views.home),
    path('foro/', views.foro),
    path('index/', views.index),
    path('perfil/', views.perfil),
    path('registro/', views.registro),
    path('test/', views.test),
    path('prueba_post/', views.post_prueba),
    path('prueba_login/', views.login_prueba),
    path('prueba_poll/',views.prueba_poll)
]