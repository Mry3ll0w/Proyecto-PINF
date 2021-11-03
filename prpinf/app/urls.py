from django.urls import path
from . import views

urlpatterns = [
    path('si/',views.si)
    path('home/', views.si)
    path('foro/', views.si)
    path('index/', views.si)
]