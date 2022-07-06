from collections import UserList
import re
from urllib import response
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from core.models import Veiculos, AuthUser, CheckList, EquipamentoSeguraca, ChecklistEquipamentoSeguranca


# ---------------------------------------------------------------------------------------------

def login_user(request):
    return render(request, 'login.html')
# ---------------------------------------------------------------------------------------------

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/inicio/')
        else:
            messages.error(request, 'Senha ou usuario invalidos')
        return redirect('/')

# ---------------------------------------------------------------------------------------------

def logout_user(request):
    logout(request)
    return redirect('/')

# ---------------------------------------------------------------------------------------------

def inicio(request):
    return render(request, 'inicio.html')

# ---------------------------------------------------------------------------------------------

def index(request):
    return render(request, 'index.html')

# ---------------------------------------------------------------------------------------------

@login_required(login_url='/login/')
def usuario(request):
    id = request.user.id
    username = request.user
    email = request.user.email
    response = {'id': id, 'username': username, 'email': email}
    return render(request, 'usuario.html', response)

# ---------------------------------------------------------------------------------------------

#@login_required(login_url='/login/')
def checklist(request):
    checklist = CheckList.objects.all()
    response = {'checklists': checklist}
    return render(request, 'checklist.html', response)

# ---------------------------------------------------------------------------------------------

#@login_required(login_url='/login/')
def detalhes(request):
    id_checklist = request.GET.get('id')
    checklist = CheckList.objects.get(id=id_checklist)
    detalhe = ChecklistEquipamentoSeguranca.objects.filter(checklist=checklist.id)
    response = {'detalhes': detalhe, 'checklist': checklist}
    return render(request, 'detalhes.html' , response)

# ---------------------------------------------------------------------------------------------

#@login_required(login_url='/login/')
def veiculos(request):
    veiculo = Veiculos.objects.all()
    response = {'veiculos': veiculo}
    return render(request, 'veiculos.html', response)

# ---------------------------------------------------------------------------------------------

@login_required(login_url='/login/')
def editar_veiculo(request):
    titulo = 'Editar veículo'
    id = request.GET.get('id')
    veiculo = Veiculos.objects.get(id=id)
    response = {'veiculo': veiculo, 'titulo': titulo}
    return render(request, 'editar-veiculos.html', response)

# ---------------------------------------------------------------------------------------------

@login_required(login_url='/login/')
def submit_veiculo(request):
    if request.POST:
        descricao_veiculo = request.POST.get('descricao_veiculo')
        id = request.POST.get('id')
        if descricao_veiculo == '':
            messages.error(request, 'O campo não pode ser vazio')
            return redirect('/veiculos/editar/?id={}' .format(id))
        if id:
            Veiculos.objects.filter(id=id).update(descricao_veiculo=descricao_veiculo)
        else:
            Veiculos.objects.create(id=id, descricao_veiculo=descricao_veiculo)
    return redirect('/veiculos/')

# ---------------------------------------------------------------------------------------------

@login_required(login_url='/login/')
def excluir_veiculo(request, id):
    usuario = request.user
    try:
        veiculo = Veiculos.objects.get(id=id)
    except Exception:
        raise Http404()
    if usuario is not None:
        veiculo.delete()
        messages.success(request, 'Veículo excluído com sucesso')
    else:
        raise Http404()
    return redirect('/veiculos/')

# ---------------------------------------------------------------------------------------------

@login_required(login_url='/login/')
def adicionar_veiculo(request):
    titulo = 'Adicionar veículo'
    response = {'titulo': titulo}        
    return render(request, 'editar-veiculos.html', response)

# ---------------------------------------------------------------------------------------------

@login_required(login_url='/login/')
def submit_adicionar_veiculo(request):
    if request.POST:        
        descricao_veiculo = request.POST.get('descricao_veiculo')
        id = request.POST.get('id')
        if descricao_veiculo == '':
            messages.error(request, 'O campo não pode ser vazio')
            return redirect('/veiculos/adicionar/')
        if id:
            Veiculos.objects.filter(id=id).update(descricao_veiculo=descricao_veiculo)
        else:
            Veiculos.objects.create(descricao_veiculo=descricao_veiculo)
        return redirect('/veiculos/')
    return render(request, 'editar-veiculos.html')

# ---------------------------------------------------------------------------------------------

#@login_required(login_url='/login/')
def equipamento(request):
    equipamentoseguraca = EquipamentoSeguraca.objects.all()
    response = {'equipamentoseguracas': equipamentoseguraca}
    return render(request, 'equipamentos.html', response)

# ---------------------------------------------------------------------------------------------

@login_required(login_url='/login/')
def editar_equipamento(request):
    titulo = 'Editar equipamento'
    id = request.GET.get('id')
    equipamentoseguraca = EquipamentoSeguraca.objects.get(id=id)
    response = {'equipamentoseguraca': equipamentoseguraca, 'titulo': titulo}
    return render(request, 'editar-equipamentos.html', response)

# ---------------------------------------------------------------------------------------------

@login_required(login_url='/login/')
def submit_equipamento(request):
    if request.POST:        
        descricao_equipamento_seguranca = request.POST.get('descricao_equipamento_seguranca')
        id = request.POST.get('id')
        if descricao_equipamento_seguranca == '':
            messages.error(request, 'O campo não pode ser vazio')
            return redirect('/equipamentos/editar/?id={}' .format(id))
        if id:
            EquipamentoSeguraca.objects.filter(id=id).update(descricao_equipamento_seguranca=descricao_equipamento_seguranca)
        else:
            EquipamentoSeguraca.objects.create(descricao_equipamento_seguranca=descricao_equipamento_seguranca)
        return redirect('/equipamentos/')
    return render(request, 'editar-equipamentos.html')

# ---------------------------------------------------------------------------------------------

@login_required(login_url='/login/')
def excluir_equipamento(request, id):
    usuario = request.user
    try:
        equipamento = EquipamentoSeguraca.objects.get(id=id)
    except Exception:
        raise Http404()
    if usuario is not None:
        equipamento.delete()
        messages.success(request, 'Equipamento excluído com sucesso')
    else:
        raise Http404()
    return redirect('/equipamentos/')

# ---------------------------------------------------------------------------------------------

@login_required(login_url='/login/')
def adicionar_equipamento(request):
    titulo = 'Adicionar equipamento'
    response = {'titulo': titulo}        
    return render(request, 'editar-equipamentos.html', response)

# ---------------------------------------------------------------------------------------------

@login_required(login_url='/login/')
def submit_adicionar_equipamento(request):
    if request.POST:        
        descricao_equipamento_seguranca = request.POST.get('descricao_equipamento_seguranca')
        id = request.POST.get('id')
        if descricao_equipamento_seguranca == '':
            messages.error(request, 'O campo não pode ser vazio')
            return redirect('/equipamentos/adicionar/')
        if id:
            EquipamentoSeguraca.objects.filter(id=id).update(descricao_equipamento_seguranca=descricao_equipamento_seguranca)
        else:
            EquipamentoSeguraca.objects.create(descricao_equipamento_seguranca=descricao_equipamento_seguranca)
        return redirect('/equipamentos/')
    return render(request, 'editar-equipamentos.html')