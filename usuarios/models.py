from django.db import models
from django.contrib.auth.models import User

class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    ordem = models.IntegerField(default=0)
    
    def __str__(self):
        return self.titulo 