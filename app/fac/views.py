from django.shortcuts import render,redirect
from django.views import generic


from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from datetime import datetime


from django.contrib.auth import authenticate

from app.base.views import SinPrivilegios

from .models import Cliente

# Create your views here.
class ClienteView(SinPrivilegios, generic.ListView):
    model = Cliente
    template_name = "fac/cliente_list.html"
    context_object_name = "obj"
    permission_required="cmp.view_cliente"