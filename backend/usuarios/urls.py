from django.urls import path
from .views import listar_usuarios, buscar_usuario_por_id

urlpatterns = [
    path('', listar_usuarios),
    path('<int:id>/', buscar_usuario_por_id),
]
