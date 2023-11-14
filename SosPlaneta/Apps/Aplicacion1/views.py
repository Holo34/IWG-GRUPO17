from django.shortcuts import render
from django.template import loader

def home(request): #Le estamos pidiendo que cuando uno busque la URL, nos devuelva una página
    return render(request, 'home1.html')

def mapa(request):
    return render(request, 'mapa.html')

def historial(request):
    return render(request, 'historial.html')

def nosotros(request):
    return render(request, "nosotros.html")

def test(request):
    return render(request, "test.html")