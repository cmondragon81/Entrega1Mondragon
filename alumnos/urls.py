from django.urls import path
from . import views

urlpatterns = [
    path('alumnos/', views.alumnos, name = "alumnos"),
    path('registro/', views.altaalumos, name= 'crearalumnos')
]