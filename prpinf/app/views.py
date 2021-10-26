from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def si(request):
    return render(request,'si.html',{'name':'tu madre L0L'})