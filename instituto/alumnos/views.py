from django.shortcuts import render

from .models import Alumno, Genero

def index(request):
    alumnos = Alumno.objects.all()
    context = {"alumnos":alumnos}
    return render(request, 'index.html', context)

def crud(request):
    alumnos = Alumno.objects.all()
    context = {"alumnos":alumnos}
    return render(request, 'alumnos_list.html', context)