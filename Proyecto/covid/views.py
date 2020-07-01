from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    if(request.method == 'POST'):
        print("1")
    return render(request, "index.html")

def ingresar(request):
    return render(request, "ingresar.html")

def registrar(request):
    return render(request, "registrar.html")

def admin(request):
    return render(request, "admin.html")