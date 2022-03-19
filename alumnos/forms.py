from django import forms

class alumnoingresar(forms.Form):
    dni=forms.IntegerField()
    clave=forms.CharField(max_length=12)
    