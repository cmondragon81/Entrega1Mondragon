from django import forms

class Profesoresalta(forms.Form):
    nombre=forms.CharField(max_length=20)
    apellido=forms.CharField(max_length=30)
    dni=forms.IntegerField()
    clave=forms.CharField(max_length=12,widget=forms.PasswordInput)
    turno_manana=forms.BooleanField(required=False, label='Turno Mañana')
    turno_tarde=forms.BooleanField(required=False)
    turno_noche=forms.BooleanField(required=False)

class Buscarprofesores(forms.Form):
    nombre=forms.CharField(max_length=20)