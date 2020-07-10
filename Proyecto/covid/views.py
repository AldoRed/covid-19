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
        dolor_toraxico = request.POST.get('dolor_toraxico','')
        odinoflagia = request.POST.get('odinoflagia','')
        mialgias = request.POST.get('mialgias','')
        calofrios = request.POST.get('calofrios','')
        cefalea = request.POST.get('cefalea','')
        diarrea = request.POST.get('diarrea','')
        anosmia = request.POST.get('anosmia','')
        ageusia = request.POST.get('ageusia','')
        
        nombres = ["tos","fiebre","dolor_toraxico","odinoflagia","mialgias","calofrios","cefalea","diarrea","anosmia","ageusia"]
        sintomas = []

        sintomas.append(tos)
        sintomas.append(fiebre)
        sintomas.append(dolor_toraxico)
        sintomas.append(odinoflagia)
        sintomas.append(mialgias)
        sintomas.append(calofrios)
        sintomas.append(cefalea)
        sintomas.append(diarrea)
        sintomas.append(anosmia)
        sintomas.append(ageusia)

        for i in range(len(sintomas)):
            if(sintomas[i] == "on"):
                sintomas[i] = nombres[i]
        

        nuevo_cliente = Clientes()
        nuevo_cliente.nombre = nombre
        nuevo_cliente.apellido = apellido
        nuevo_cliente.correo = correo
        nuevo_cliente.numero = celular
        nuevo_cliente.sintomas = sintomas
        nuevo_cliente.comentarios = "Aun no tienes comentarios"
        nuevo_cliente.save()

    return render(request, "index.html")

def ingresar(request):
    if(request.method == 'POST'):
        email = request.POST.get('email','')
        cliente = Clientes.objects.get(correo=email)

        if(cliente == ""):
            return render(request, "ingresar.html")
            
        context = {"nombre":cliente.nombre,
                    "apellido":cliente.apellido,
                    "correo":cliente.correo,
                    "numero":cliente.numero,
                    "comentario":cliente.comentarios}

        return render(request, "inicio.html", context)
    return render(request, "ingresar.html")

def registrar(request):
    return render(request, "registrar.html")

def admin(request):
    return render(request, "admin.html")
