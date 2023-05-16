from .models import TasksModel
from .forms import TasksModelForm
from django.shortcuts import render, HttpResponse
import datetime

data = datetime.date.today()

def index(request):

    tarefas = []

    context = {'listaTarefas': tarefas }       
    tarefas = TasksModel.objects.all()

    for tarefa in tarefas:
        if(tarefa.data == data):
            context['listaTarefas'].append(tarefa)  

    return render(request,'index.html', context)

def create(request):     
    if request.method == 'POST':    
        form = TasksModelForm(request.POST)
        if form.is_valid():
            tarefa = form.data['tarefa']
            descricao = form.data['descricao']
            data = form.data['data']

            form.save()

            form = TasksModelForm()
            return render(request,' create.html', {'form': form})
           
        return HttpResponse('Registro Inválido')
    else:
        form = TasksModelForm   
        return render(request,'create.html', {'form': form})
    
def delete(request, id):
    tarefa = TasksModel.objects.get(pk=id) 

    if tarefa != None:
        tarefa.delete()
    return index(request)

def update(request, id): 
     tarefa = TasksModel.objects.get(pk=id)
     return render(request,'update.html', {'form': tarefa})
    
def edit(request):       
        
        if request.method == 'POST': 
            form = TasksModelForm(request.POST) 
               
            if form.is_valid():
                
                task = TasksModel()
                task.id = form.data['id']
                task.tarefa = form.data['tarefa']
                task.detalhes = form.data['detalhes']
                task.data = form.data['data']

                task.save()
                
                form = TasksModelForm   
                return index(request)