from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import Task
from .forms import TaskForm

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks':tasks,'form':form}
    return render(request,'list.html',context)

def updateTask(request,pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}

    return render(request,'update_task.html',context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request,'delete.html', context)








'''def index(request):
    tasks=Task.objects.all()
    context={'tasks':tasks}
    return render(request,'tasks/list.html',context)
class TaskList(ListView):
    model = Todo
    context_object_name = 'task'
class TaskDetails(DetailView):
    model = Todo
    context_object_name = 'task'
    template_name = 'todo/task.html'
def delete(requuest):
    return render(requuest,'delete')
class TaskCreate(CreateView):
    model=Task
    field='__all__'
    success_url = reverse_lazy('taks')'''


