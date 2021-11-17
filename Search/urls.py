from django.urls import path

from . import views

urlpatterns = [
    path('', views.especializacion, name="especializacion"),
    path('tabla/? <str:id>', views.MostrarTabla, name='tabla'),
    path('tabla/mapa/? <str:id>', views.showMapa, name='mapa'),
    path('servicio/datos/', views.BuscarView, name='buscar'),
]