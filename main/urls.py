from django.urls import path
from . import views

urlpatterns = [
    path('accounts/cadastro', views.register, name='cadastro'),
    path('', views.HomeView.as_view(), name='home'),
    path('accounts/login', views.login, name='login'),
    
]
