from django.shortcuts import redirect, render
from .forms import Profesoresalta, Buscarprofesores
from .models import Profesores

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
 