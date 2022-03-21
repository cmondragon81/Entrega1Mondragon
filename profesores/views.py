from django.shortcuts import redirect, render
from .forms import Profesoresalta, Buscarprofesores,Cursos_f
from .models import Profesores, Cursos

# Create your views here.
def profesores(request):

    if request.method =='POST':
        form=Profesoresalta(request.POST)

        if form.is_valid():
            datos=form.cleaned_data
            guardar=Profesores(
                nombre=datos['nombre'],
                apellido=datos['apellido'],
                dni=datos['dni'],
                clave=datos['clave'],
                materia=datos['materia'],
                turno_manana=datos['turno_manana'],
                turno_tarde=datos['turno_tarde'],
                turno_noche=datos['turno_noche']
            )
            guardar.save()
            return redirect ('profesores')


    form=Profesoresalta()
    return render (request, 'profesores.html', {'form':form})

def buscarprofesor(request):

    busqueda = request.GET.get('nombre',None)

    if busqueda is not None:
        profesores = Profesores.objects.filter(nombre__icontains=busqueda)
        form=Buscarprofesores()
        return render (request, 'buscarprofesor.html', {'form':form, 'profesores':profesores})
    
    form=Buscarprofesores()
    return render (request, 'buscarprofesor.html', {'form':form})

def crear_curso(request):
    
    if request.method =='POST':
        form=Cursos_f(request.POST)

        if form.is_valid():
            datos=form.cleaned_data
            guardar=Cursos(
                materia=datos['materia'],
                turno_manana=datos['turno_manana'],
                turno_tarde=datos['turno_tarde'],
                turno_noche=datos['turno_noche'],
                cupos=datos['cupos']
            )
            guardar.save()
            return redirect ('crear')

    
    form=Cursos_f()
    return render (request, 'crear_curso.html',{'form':form})