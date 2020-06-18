from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('inicio',views.index),
    path('ingresar',views.ingresar),
    path('registro',views.registrar),
    path('administracion',views.admin),
]