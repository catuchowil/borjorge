from re import template
from django.shortcuts import render

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Categoria, SubCategoria 
from .forms import CategoriaForm, SubCategoriaForm

# Create your views here.
class CategoriaView(LoginRequiredMixin,generic.ListView):
    model = Categoria
    template_name = 'inv/categoria_list.html'
    context_object_name = 'obj'
    login_url = 'base:login'


class CategoriaNew(LoginRequiredMixin,generic.CreateView):
    model = Categoria
    template_name = 'inv/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy('inv:categoria_list')
    login_url = 'base:login'

    def form_valid(self,form):
        form.instance.uc = self.request.user
        return super().form_valid(form)



class CategoriaEdit(LoginRequiredMixin,generic.UpdateView):
    model = Categoria
    template_name = 'inv/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy('inv:categoria_list')
    login_url = 'base:login'

    def form_valid(self,form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


class CategoriaDel(LoginRequiredMixin,generic.DeleteView):
    model = Categoria
    template_name = 'inv/catalogos_del.html'
    contex_object_name = 'obj'
    success_url = reverse_lazy('inv:categoria_list')



class SubCategoriaView(LoginRequiredMixin,generic.ListView):
    model = SubCategoria
    template_name = 'inv/subcategoria_list.html'
    context_object_name = 'obj'
    login_url = 'base:login'



class SubCategoriaNew(LoginRequiredMixin,generic.CreateView):
    model = SubCategoria
    template_name = 'inv/subcategoria_form.html'
    context_object_name = 'obj'
    form_class = SubCategoriaForm
    success_url = reverse_lazy('inv:subcategoria_list')
    login_url = 'base:login'

    def form_valid(self,form):
        form.instance.uc = self.request.user
        return super().form_valid(form)