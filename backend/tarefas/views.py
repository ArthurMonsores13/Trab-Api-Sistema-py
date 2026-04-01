from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Tarefa
from datetime import datetime

def index(request):
    return render(request, 'index.html')

def listar_tarefas(request):
    tarefa = Tarefa.objects.all().values()
    return JsonResponse(list(tarefa), safe=False)

def criar_tarefa(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao', '')
        status = request.POST.get('status', 'ABERTA')
        data_entrega_str = request.POST.get('data_entrega')
        
        status_map = {
            'pendente': 'ABERTA',
            'em_progresso': 'EM_ANDAMENTO',
            'concluida': 'CONCLUIDA'
        }
        status_modelo = status_map.get(status, 'ABERTA')
        
        data_entrega = datetime.strptime(data_entrega_str, '%Y-%m-%d').date()
        
        
        try:
            tarefa = Tarefa.objects.create(
                titulo=titulo,
                descricao=descricao,
                status=status_modelo,
                data_entrega=data_entrega
            )
            return render(request, 'criar_tarefa.html', {
                'mensagem': f'Tarefa "{titulo}" criada com sucesso! ✨'
            })
        except Exception as e:
            return render(request, 'criar_tarefa.html', {
                'erro': f'Erro ao criar tarefa: {str(e)}'
            })
    
    return render(request, 'criar_tarefa.html')
