from django.urls import path
# from .views import Deletar
from .views import adicionar_tarefa_view, apagarTarefaView,apagarTodasAllView, mover_para_cima_view, mover_para_baixo_view


urlpatterns = [
    # path('<int:pk>/deletar/', Deletar.as_view(), name='deletar_tarefa'),
    path('adicionarTarefa/', adicionar_tarefa_view, name='adicionarTarefa'),
    path('apagarTarefa/<int:id>', apagarTarefaView, name='apagarTarefa'),
    path('apagarTarefas/', apagarTodasAllView, name='apagarTarefas'),
    path('moverCima/<int:id>/', mover_para_cima_view, name='moverCima'),
    path('moverBaixo/<int:id>/', mover_para_baixo_view, name='moverBaixo')

]