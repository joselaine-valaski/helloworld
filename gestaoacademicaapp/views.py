from django.shortcuts import render, get_object_or_404, redirect
from .models import Matricula

def listaMatriculas(request):

    listadisciplina = Matricula.objects.all

    return render(request, 'gestaoacademicaapp/index.html', {'disciplinas':listadisciplina})

def fazerMatricula(request, id):
    matriculardisciplina = get_object_or_404(Matricula, pk=id)

    if(matriculardisciplina.status == 'prevista'):
        matriculardisciplina.status = 'matriculado'

    matriculardisciplina.save()

    return redirect('/')
