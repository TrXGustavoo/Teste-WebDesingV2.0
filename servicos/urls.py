from django.urls import path
from .views import DietasView, TreinoView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('dietas/', login_required(DietasView.as_view()), name='dietas'),
    path('treino/', login_required(TreinoView.as_view()), name='treinos'),
]
