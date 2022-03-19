from django.shortcuts import render
from .forms import alumnoingresar

# Create your views here.
def alumnos(request):
    form=alumnoingresar()
    return render (request, 'home_alumnos.html', {'form':form})

def altaalumos(request):
    form=None
    return render (request, 'crearalumnos.html',{'form':form})