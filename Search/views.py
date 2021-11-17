from django import template
from django.contrib.auth import views
from django.http import HttpResponse
from .forms import UserRegisterForm
from .forms import *
from .models import *
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.contrib import messages

lista= ['Cardiología','Patología','Fisiatría','Dermatología','Neumología','Infectología','Oncohematología.']

def index(request):
    return render(request,'home.html')   
   
def start(request):
    return render(request,"home.html")

def prueba(request):
    return render(request, "prueba.html")

def mapa(request):
    return render(request, "map.html")

def login(request):
    return render(request, "login.html")

def contacto(request):
    return render(request, "contacto.html")
    
def prueba_contact(request):
    return render(request, 'temp.html')

def especializacion(request):
    especie= servicio.objects.all()           
    return render(request, "especializacion.html", {
        'lista': valores_unicos()
    })
    
def valores_unicos():
    lista=[]
    servicios = servicio.objects.values('Especialidad').order_by('Nombre').distinct()
    for i in servicios:
        name=i['Especialidad'].replace('/',"")
        lista.append(name)
    return lista

def MostrarTabla(request, id):
    print(id)
    servicios = servicio.objects.filter(Especialidad__icontains = id).order_by("Nombre")
    return render(request,"info-eps.html",{
        "servicio":servicios,
        "id":id
    })
    
def showMapa(request, id):
    id = servicio.objects.filter(ID = id)
    return render(request, "map.html",{
        'id': id[0].Especialidad,
        'dire': id[0].Direccion,
        'name': id[0].Nombre,
        'correo': id[0].Correo,
        'tipo':id[0].tipo,
        'meto':id[0].Metodologia,
        'address': [float(id[0].Latitude) , float(id[0].Longitude)]
    })
   
def ShowInformacion(request):
    return render(request, "informacion.html")

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            form.save()
    else:
        form = UserRegisterForm
    context = {'form':form}
    return render(request, 'register.html', context)
  
        
def afiliaciones(request):
    return render(request, "afiliaciones.html")
    

def BuscarView(request, *args, **kwargs):
    buscar = request.POST['buscalo']
    servicios = servicio.objects.filter(Especialidad__icontains = buscar)       
    return render(request,"info-eps.html",{
        "servicio":servicios,
        "id": servicios[0].Especialidad
    })

