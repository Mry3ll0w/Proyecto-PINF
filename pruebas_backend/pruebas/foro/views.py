from django.shortcuts import render,redirect
from django.http import HttpResponse

def foro(request):
    if request.method == 'GET':
        return render(request,'foro.html',)