from django import template
from django.contrib.auth import views
from django.http import HttpResponse
from .forms import UserRegisterForm
from .forms import *
from .models import *
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect,render
from django.contrib import messages
from geopy.geocoders import Nominatim
#from django.utils import simplejson
from json import dumps

lista= ['Cardiologia','Patología','Fisiatría','Dermatología','Neumología','Infectología','Oncohematología.']#[i for i in range(1,6)]
direcciones=["Carrera 48 # 70 – 38","Carrera 74 # 76-91","Carrera A 42 G # 80 – 115","Carrera 74 # 76-91"]
direccion="Carrera 74 # 76-91"

def index(request):
    return render(request,"home.html")
   

def start(request):
    return render(request,"home.html")

def prueba(request):
    return render(request, "prueba.html")

def mapa(request):
    return render(request, "map.html")

def login(request):
    return render(request, "login.html")

def contact(request):
    return render(request, "contact.html",{
        'lista':lista
    })
    
def showMapa(request, id): 
    return render(request, "map.html",{
        'direcciones': ParametersMap(direccion),
        'id':id
    })

def  ShowQR(request):
    return render(request, "QR.html")

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


def List2Dic(lista):
    geo = Nominatim(user_agent='MyApp')
    meansures=[]
    for address in lista:
        loc = geo.geocode(f'{address}, Barranquilla')
        s={'lat':loc.latitude, 'lng': loc.longitude }
        # print(s)
        meansures.append(s)
    return meansures
    
def ParametersMap(direccion):
    measures=[]
    geo = Nominatim(user_agent='MyApp')
    loc = geo.geocode(f'{direccion}, Barranquilla')
    measures.extend([loc.latitude,loc.longitude])
    print(measures)
    return measures        
        
def afiliaciones(request):
    return render(request, "afiliaciones.html")