from django.urls import path
from .views import index, listar_tarefas, criar_tarefa

urlpatterns = [
    path('', index),
    path('tarefas/', listar_tarefas),
    path('tarefas/criar/', criar_tarefa),
]
