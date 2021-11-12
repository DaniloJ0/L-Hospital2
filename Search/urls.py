from django.urls import path

from . import views

urlpatterns = [
    path('', views.contact, name="contact"),
    path('mapa/?P<str:id>', views.showMapa, name='mapa'),
]