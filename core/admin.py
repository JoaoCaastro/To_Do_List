from django.contrib import admin
from .models import TasksModel

class TasksModelAdmin(admin.ModelAdmin):
    list_display = ('tarefa','descricao','data','cadastrado_em')
    date_hierarchy = 'data'
    search_fields = ('tarefa','data')

admin.site.register(TasksModel, TasksModelAdmin)