
from django.urls import path

from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [

    path('',views.index, name='index'),
    path('infraestructura/',views.infraestructura, name='infraestructura'),
    path('actividad/',views.actividad, name='actividad'),
    path('historia/',views.nuestraHistoria, name='historia'),
    path('IniciarSesion/',views.IniciarSesion, name='IniciarSesion'),
]