from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


class DietasView(TemplateView):
    template_name = 'dietas.html'

class TreinoView(TemplateView):
    template_name = 'treinos.html'

class PrimeiraView(TemplateView):
    template_name = 'primeira.html'
