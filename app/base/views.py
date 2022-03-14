from re import template
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# Create your views here.
class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'base/home.html'
    login_url = 'base:login'



class HomeSinPrivilegios(LoginRequiredMixin,generic.TemplateView):
    template_name = 'base/sin_privilegios.html'
    login_url = 'base_login'



class SinPrivilegios(LoginRequiredMixin,PermissionRequiredMixin):
    
    login_url = 'base:login'
    raise_exception = False
    redirect_field_name = "redirect_to"

    def handle_no_permission(self):

        from django.contrib.auth.models import AnonymousUser

        if not self.request.user == AnonymousUser():
            self.login_url = 'base:sin_privilegios'

        return HttpResponseRedirect(reverse_lazy(self.login_url))