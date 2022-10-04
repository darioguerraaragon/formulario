from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def login(request):
    return render(request,'autenticacion/registrarse.html')

def prueba(request):
    nombre = request.get['nombre']
    apellidos=request.get['apellidos']
    telefono=request.get['tfno']
    email=request.get['email']
    return render(request,'autenticado.html'),{'nombre':nombre,'apellidos':apellidos,'tfno':telefono,'email':email}