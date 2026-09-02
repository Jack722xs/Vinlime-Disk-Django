from django.shortcuts import render
from django.http import HttpResponse


def second_home(request):
    return HttpResponse("<h1>Bienvenido a Vinlume 2 Django</h1>")

def saludo(request):
    salida = "<h1>segunda app</h1>"
    return HttpResponse(salida)
