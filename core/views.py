from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("<h1>¡Hola! Mi primera vista en Django funciona.</h1>")


# Create your views here.
