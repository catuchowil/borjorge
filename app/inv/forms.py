from dataclasses import field
from tkinter import Widget
from django import forms 
from .models import Categoria

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ['descripcion','estado']
        labels = {'descripcion':'Descripción de la Categoría', 'estado':'Estado'}
        Widget = {'descripcion':forms.TextInput(
             attrs = {
                    'placeholder':'Ingrese texto',
                    #'class':'form-control',
                    'autocomplete':'off',
                    'autofocus':True
                },
        )}

    # -- Esto lo hacemos para que cada campo asuma la clase form-crontrol    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})