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
    
class SegundaView(TemplateView):
    template_name = 'segunda.html'
        
class TerceiraView(TemplateView):
    template_name = 'terceira.html'
    
class QuartaView(TemplateView):
    template_name = 'quarta.html'
    
class QuintaView(TemplateView):
    template_name = 'quinta.html'
class SextaView(TemplateView):
    template_name = 'sexta.html'
    
class SetimaView(TemplateView):
    template_name = 'setima.html'
class OitavaView(TemplateView):
    template_name = 'oitava.html'
    
class NonaView(TemplateView):
    template_name = 'nona.html'
class DecimaView(TemplateView):
    template_name = 'decima.html'
    
class DecimaPrimeiraView(TemplateView):
    template_name = 'decimaprimeira.html'
class DecimaSegundaView(TemplateView):
    template_name = 'decimasegunda.html'

class IMCView(TemplateView):
    template_name = 'IMC.html'