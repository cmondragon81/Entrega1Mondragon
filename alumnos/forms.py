from django import forms

class alumnoingresar(forms.Form):
    dni=forms.IntegerField()
    clave=forms.CharField(max_length=12, widget=forms.PasswordInput)
    

class alumnoregistrar(forms.Form):
    nombre=forms.CharField(max_length=20)
    apellido=forms.CharField(max_length=40)
    dni=forms.IntegerField()
    clave=forms.CharField(max_length= 12, widget=forms.PasswordInput)
    email=forms.EmailField()
    telefono=forms.IntegerField()
    direccion=forms.CharField(max_length=50)
    tutor=forms.CharField(max_length=50)
    tutor_telefono=forms.IntegerField()
    tutor_email=forms.EmailField()
 