from django.shortcuts import render
from django.http import HttpResponse
import datetime


def inicio(request):
    return HttpResponse("<h1>Bienvenido a Vinlume Django</h1>")

def ahora(request):
    hora = datetime.datetime.now()
    salida = "<b> Fecha y hora actual: {}</b>". format(hora)
    return HttpResponse(salida)

