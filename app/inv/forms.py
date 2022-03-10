from dataclasses import field
from tkinter import Widget
from django import forms 
from .models import Categoria,SubCategoria, Marca

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



class SubCategoriaForm(forms.ModelForm):
    
    #--Esto ne sirve para que se aplique un filtro en el combo que se genera para que una categoríaincativa
    #--No se muestre al usuario y no se pueda generar una subcategoría
    categoria =forms.ModelChoiceField(queryset = Categoria.objects.filter(estado=True).order_by('descripcion'))

    class Meta:
        model = SubCategoria
        fields = ['categoria','descripcion','estado']
        labels = {'descripcion':'SubCategoría', 'estado':'Estado'}
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

        self.fields['categoria'].empty_label = "Seleccione Categoría"
        self.fields['estado'].widget.attrs.update({'class':'custom-control custom-checkbox small'})



class MarcaForm(forms.ModelForm):
    class Meta:
        model=Marca
        fields = ['descripcion','estado']
        labels= {'descripcion': "Descripción de la Marca",
                "estado":"Estado"}
        widget={'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
