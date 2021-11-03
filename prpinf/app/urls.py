from django.urls import path
from . import views

urlpatterns = [
    path('si/',views.si),
    path('home/', views.home),
    path('foro/', views.foro),
    path('index/', views.index),
]