from importlib.resources import contents
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.views.generic import TemplateView
from .forms import NovoUsuarioForm
from django.contrib import messages


class HomeView(TemplateView):
    template_name = 'index.html'

def register(request):
    if request.method == 'POST':
        form =  NovoUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dietas')
        else:
            messages.error(request, 'Erro no cadastro')
    form = NovoUsuarioForm()
    context = {'form': form}
    return render(request, template_name='cadastro.html',context=context)