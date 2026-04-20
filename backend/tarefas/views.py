from django.http import JsonResponse
from django.shortcuts import render
from .models import Tarefa
from usuarios.models import Usuario
from datetime import datetime


def index(request):
    return render(request, 'index.html')


def listar_tarefas(request):
    tarefas = Tarefa.objects.select_related('usuario_responsavel').all()
    resultado = []
    for tarefa in tarefas:
        resultado.append({
            'id': tarefa.id,
            'titulo': tarefa.titulo,
            'descricao': tarefa.descricao,
            'status': tarefa.status,
            'data_criacao': tarefa.data_criacao,
            'data_entrega': tarefa.data_entrega,
            'usuario_responsavel_nome': tarefa.usuario_responsavel.nome if tarefa.usuario_responsavel else None,
        })
    return JsonResponse(resultado, safe=False)


def criar_tarefa(request):
    usuarios = Usuario.objects.filter(ativo=True)

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao', '')
        status = request.POST.get('status', 'ABERTA')
        data_entrega_str = request.POST.get('data_entrega')
        usuario_id = request.POST.get('usuario_responsavel')

        status_map = {
            'pendente': 'ABERTA',
            'em_progresso': 'EM_ANDAMENTO',
            'concluida': 'CONCLUIDA'
        }
        status_modelo = status_map.get(status, 'ABERTA')

        if not data_entrega_str:
            return render(request, 'criar_tarefa.html', {
                'erro': 'A data de entrega é obrigatória.',
                'usuarios': usuarios,
            })
        data_entrega = datetime.strptime(data_entrega_str, '%Y-%m-%d').date()

        usuario = None
        if usuario_id:
            try:
                usuario = Usuario.objects.get(pk=usuario_id)
            except Usuario.DoesNotExist:
                pass

        try:
            tarefa = Tarefa.objects.create(
                titulo=titulo,
                descricao=descricao,
                status=status_modelo,
                data_entrega=data_entrega,
                usuario_responsavel=usuario
            )
            return render(request, 'criar_tarefa.html', {
                'mensagem': f'Tarefa "{titulo}" criada com sucesso!',
                'usuarios': usuarios,
            })
        except Exception as e:
            return render(request, 'criar_tarefa.html', {
                'erro': f'Erro ao criar tarefa: {str(e)}',
                'usuarios': usuarios,
            })

    return render(request, 'criar_tarefa.html', {'usuarios': usuarios})
