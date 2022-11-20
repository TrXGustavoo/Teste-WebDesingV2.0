from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('dietas/', DietasView.as_view(), name='dietas'),
    path('treino/', login_required(TreinoView.as_view()), name='treinos'),
    path('próta/', login_required(PrimeiraView.as_view()), name='primeira'),
    path('Deftéra/', login_required(SegundaView.as_view()), name='segunda'),
    path('trítos/', login_required(TerceiraView.as_view()), name='terceira'),
    path('tétartos/', login_required(QuartaView.as_view()), name='quarta'),
    path('Pémpti/', login_required(QuintaView.as_view()), name='quinta'),
    path('Paraskeví/', login_required(SextaView.as_view()), name='sexta'),
    path('évdomos/', login_required(SetimaView.as_view()), name='setima'),
    path('oktáva/', login_required(OitavaView.as_view()), name='oitava'),
    path('énatos/', login_required(NonaView.as_view()), name='nona'),
    path('apó páno/', login_required(DecimaView.as_view()), name='decima'),
    path('IMC/', login_required(IMCView.as_view()), name='IMC'),
]
