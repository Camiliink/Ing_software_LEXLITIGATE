from django.shortcuts import render
from .models import Solicitud
# Create your views here.


def home(request):
    solicitudes = Solicitud.objects.all()
    return render(request, "gestion_formulario.html",{"solicitudes": solicitudes})