from django.shortcuts import render,redirect
from .models import Task
from django.views.generic import DeleteView,DetailView,UpdateView
from .forms import TaskForm


class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail_view.html'
    context_object_name = 'article'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'create.html'
    form_class = TaskForm


class TaskDeleteView(DeleteView):
    model = Task
    success_url = 'task_detail'
    template_name = 'deletetask.html'


def index(request):
    return render(request,'index.html')


def addtask(request):
    return render(request,'addtask.html')


def edittask(request):
    tasks = Task.objects.all()
    return render(request,'edittask.html',{'title':'Главные задачи на неделю','tasks':tasks})


def create(request):
    error = ""
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/edittask')
        else:
            error = "Форма заполнена некорректно!"

    form = TaskForm()
    context = {
        "form":form,
        "error":error
    }
    return render(request,'create.html',context)


