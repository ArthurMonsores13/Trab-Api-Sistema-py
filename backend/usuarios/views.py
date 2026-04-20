from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Usuario


def listar_usuarios(request):
    usuarios = Usuario.objects.all().values('id', 'nome', 'email', 'ativo', 'data_criacao')
    return JsonResponse(list(usuarios), safe=False)


def buscar_usuario_por_id(request, id):
    try:
        usuario = Usuario.objects.get(pk=id)
    except Usuario.DoesNotExist:
        return JsonResponse({'erro': 'nada'}, status=404)

    return JsonResponse({
        'id': usuario.id,
        'nome': usuario.nome,
        'email': usuario.email,
        'ativo': usuario.ativo,
        'data_criacao': usuario.data_criacao,
    })
