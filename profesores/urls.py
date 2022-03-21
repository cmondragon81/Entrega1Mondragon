from django.urls import path
from . import views

urlpatterns = [
    path('profesores/', views.profesores, name = "profesores"),
    path('profesores/listar/',views.buscarprofesor, name = 'listar'),
    path('profesores/cursos/',views.crear_curso, name = 'crear'),
]