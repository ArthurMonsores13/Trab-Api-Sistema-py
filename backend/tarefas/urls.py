from django.urls import path
from .views import (
    index, listar_tarefas, criar_tarefa,
    tarefas_por_prioridade, tarefa_por_id, tarefas_urgentes_abertas,
    tarefas_atrasadas, buscar_tarefas,
)

urlpatterns = [
    path('', index),
    path('tarefas/', listar_tarefas),
    path('tarefas/criar/', criar_tarefa),
    path('tarefas/atrasadas/', tarefas_atrasadas),
    path('tarefas/buscar/', buscar_tarefas),
    path('tarefas/prioridade/<str:prioridade>/', tarefas_por_prioridade),
    path('tarefas/urgentes-abertas/', tarefas_urgentes_abertas),
    path('tarefas/<int:id>/', tarefa_por_id),
]
