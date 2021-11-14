from django.urls import path

from . import views

urlpatterns = [
    path('', views.especializacion, name="especializacion"),
    path('mapa/?P<str:id>', views.showMapa, name='mapa'),
]