from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import *

class CarroForm(ModelForm):
    class Meta:
        model = Carro
        fields = ['modelo', 'marca', 'ano', 'valor', 'data_cadastro']


def cadastrar_carro(request, template_name='carro_form.html'):
    form = CarroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('carro_list')
    return render(request, template_name, {'form':form})

def listar_carro(request, template_name='carro_list.html'):
    query = request.GET.get("busca")
    #modelo__iexact=query
    if query:
        carro = Carro.objects.filter(modelo__icontains=query)
    else:
        carro = Carro.objects.all()
    return render(request, template_name, {'lista':carro})

def editar_carro(request, pk, template_name='carro_form.html'):
    carro = get_object_or_404(Carro, pk=pk)
    if request.method == 'POST':
        form = CarroForm(request.POST, instance=carro)
        if form.is_valid():
            form.save()
            return redirect('carro_list')
    else:
        form = CarroForm(instance=carro)
    return render(request, template_name, {'form':form})

def remover_carro(request, pk, template_name='carro_delete.html'):
    carro = Carro.objects.get(pk=pk)
    if request.method == 'POST':
        carro.delete()
        return redirect('carro_list')
    return render(request, template_name, {'carro': carro})


