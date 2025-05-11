from django.urls import path
# from .views import Deletar
from .views import adicionar_tarefa_view, apagarTarefaView


urlpatterns = [
    # path('<int:pk>/deletar/', Deletar.as_view(), name='deletar_tarefa'),
    path('adicionarTarefa/', adicionar_tarefa_view, name='adicionarTarefa'),
    path('apagarTarefa/<int:id>', apagarTarefaView, name='apagarTarefa')
]