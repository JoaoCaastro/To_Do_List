from django.db import models

class TasksModel(models.Model):
    id = models.IntegerField().primary_key
    tarefa = models.CharField(max_length=50)
    descricao = models.CharField(max_length=500)
    data = models.DateField()
    cadastrado_em = models.DateTimeField(
        verbose_name='cadastrado em', 
        auto_now_add=False, auto_now=True
    )

    def __str__(self):
        return self.tarefa
    
    class Meta:
        verbose_name_plural = 'Tarefas'
        verbose_name = 'Tarefa'
        ordering = ('data','cadastrado_em')
