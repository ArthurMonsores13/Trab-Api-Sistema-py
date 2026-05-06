from django.urls import path
from .views import (
    index, listar_tarefas, criar_tarefa,
    tarefas_por_prioridade, tarefa_por_id, tarefas_urgentes_abertas,
)

urlpatterns = [
    path('', index),
    path('tarefas/', listar_tarefas),
    path('tarefas/criar/', criar_tarefa),
    path('tarefas/prioridade/<str:prioridade>/', tarefas_por_prioridade),
    path('tarefas/<int:id>/', tarefa_por_id),
    path('tarefas/urgentes-abertas/', tarefas_urgentes_abertas),
]
