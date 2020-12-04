from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import Hospitalform
from .models import Hospital
# Create your views here.

def index(request):
    #return HttpResponse('<h1>Aqui é o index<h1>')
    return render(request, 'hospitais/index.html')

def hospitais(request):
    hospitais = Hospital.objects.all()
    busca = request.GET.get('search')
    if busca:
    	hospitais = Hospital.objects.filter(nome_hospital__icontains = busca)
    return render(request, 'hospitais/hospitais.html',  {'hospitais':hospitais})


def editar(request, id):
	hosp = get_object_or_404(Hospital, pk=id)
	form = Hospitalform(instance=hosp)

	if(request.method == "POST"):
		form = Hospitalform(request.POST, request.FILES, instance=hosp)

		if form.is_valid():
			form.save()
			return redirect('hospitais')

		else:

			return render(request, 'hospitais/editar_hospitais.html', {'form':form, 'hosp':hosp})

	else:

		return render(request, 'hospitais/editar_hospitais.html', {'form':form, 'hosp':hosp})


def criar_hospitais(request):
    form = Hospitalform(request.POST)
    if request.method == "POST":
    	form = Hospitalform(request.POST, request.FILES)
    	if form.is_valid():
    		hosp = form.save()
    		hosp.save()
    		form = Hospitalform
    return render(request, 'hospitais/criar_hospitais.html', {'form':form})



def deletar(request, id):
	hosp = get_object_or_404(Hospital, pk=id)
	if request.method == "POST":
		hosp.delete()
		return redirect('hospitais')
	return render(request, "hospitais/deletar_hospital.html", {'hosp':hosp})
	