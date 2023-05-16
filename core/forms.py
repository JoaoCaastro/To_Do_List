from .models import TasksModel
from django.forms import ModelForm

class TasksModelForm(ModelForm):
    class Meta:
        model = TasksModel
        fields = ['id','tarefa','descricao','data']