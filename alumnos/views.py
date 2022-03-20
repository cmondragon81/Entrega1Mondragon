from django.shortcuts import redirect, render
from .forms import alumnoingresar, alumnoregistrar
from .models import Alumnos

# Create your views here.
def alumnos(request):
    form=alumnoingresar()
    return render (request, 'home_alumnos.html', {'form':form})

def altaalumos(request):

    if request.method == "POST":
        form = alumnoregistrar(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            guardar=Alumnos(nombre=data['nombre'], apellido=data['apellido'], dni=data['dni'], clave=data['clave'], email=data['email'],telefono=data['telefono'], direccion=data['direccion'], tutor=data['tutor'], tutor_telefono=data['tutor_telefono'], tutor_email=data['tutor_email'])
            guardar.save()
            return redirect ('crearalumnos')

    form=alumnoregistrar
    return render (request, 'crearalumnos.html',{'form':form})