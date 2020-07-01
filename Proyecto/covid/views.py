from django.shortcuts import render
from django.http import HttpResponse
from .models import Clientes

# Create your views here.

def index(request):
    if(request.method == 'POST'):
        nombre = request.POST.get('nombre','')
        apellido = request.POST.get('apellido','')
        correo = request.POST.get('email','')
        celular = request.POST.get('celular','')
        tos = request.POST.get('tos','')
        fiebre = request.POST.get('fiebre','')

        sintomas = []

        sintomas.append(tos)
        sintomas.append(fiebre)

        nuevo_cliente = Clientes()
        nuevo_cliente.nombre = nombre
        nuevo_cliente.apellido = apellido
        nuevo_cliente.correo = correo
        nuevo_cliente.numero = celular
        nuevo_cliente.sintomas = sintomas
        nuevo_cliente.save()

    return render(request, "index.html")

def ingresar(request):
    return render(request, "ingresar.html")

def registrar(request):
    return render(request, "registrar.html")

def admin(request):
    return render(request, "admin.html")