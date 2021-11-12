"""LHospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView,LogoutView
from Search import views
import Search


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.index, name='index'),
    path('', LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('logout/',LogoutView.as_view(template_name = 'logout.html'), name = 'logout'),
    path('register/', views.register, name='register'),
    # path('Contactenos/', views.contact, name="contact"),
    path('Contactenos/', include('Search.urls')),
    # path('mapa/', views.showMapa, name='mapa'),
    path('Q&R/', views.ShowQR, name='questions'),
    path('afiliaciones/', views.afiliaciones, name='afilia'),
]

urlpatterns +=staticfiles_urlpatterns()
