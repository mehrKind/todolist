from django.shortcuts import render, redirect
from .models import TodoItem
from django.contrib.auth.decorators import login_required
from .forms import TodoItemForm


def home_view(request):
    return render(request, 'todoapp/home.html')


@login_required(login_url='/accounts/login')
def todo_list_item(request):
    user = request.user
    query = TodoItem.objects.filter(owner=user)
    if request.method == 'POST':
        cheked_list = request.POST.getlist('checked')
        cheked_list = [int(i) for i in cheked_list]
        # print(cheked_list)
        for todo_item in query:
            if todo_item.id in cheked_list:
                TodoItem.objects.filter(id=todo_item.id).update(checked=True)
            else:
                TodoItem.objects.filter(id=todo_item.id).update(checked=False)
        return redirect('/list')
    
    todolist_len = len(query)

    return render(request, 'todoapp/todo_list.html', {'todolist': query, 'todolist_len':todolist_len})


@login_required(login_url='/accounts/login')
def todoitemCreate(request):
    user = request.user
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = user
            instance.save()
            return redirect('todoapp:todo_list')
    user = request.user
    form = TodoItemForm()

    return render(request, 'todoapp/create_todo_item.html', {'form': form})


def delet_item(request, id):
    try:
        item = TodoItem.objects.get(id=id)
    except:
        return redirect('todoapp:todo_list')
    if item.owner == request.user:
        item.delete()
        return redirect('todoapp:todo_list')
    else:
        return redirect('todoapp:todo_list')
