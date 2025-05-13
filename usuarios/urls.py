from django.urls import path
from .views import adicionar_tarefa_view, apagarTarefaView,apagarTodasAllView, mover_para_cima_view, mover_para_baixo_view


urlpatterns = [
    path('adicionarTarefa/', adicionar_tarefa_view, name='adicionarTarefa'),
    path('apagarTarefa/<int:id>', apagarTarefaView, name='apagarTarefa'),
    path('apagarTarefas/', apagarTodasAllView, name='apagarTarefas'),
    path('moverCima/<int:id>/', mover_para_cima_view, name='moverCima'),
    path('moverBaixo/<int:id>/', mover_para_baixo_view, name='moverBaixo')

]