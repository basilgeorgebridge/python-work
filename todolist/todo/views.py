from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import todo

# Create your views here.

def show(request):
    all_todo_items = todo.objects.all()
    return render(request, 'index.html',
    {'all_items':all_todo_items })

def add(request):
    x = request.POST['content']
    new_item = todo(content = x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')

def delete(request, id):
    y = todo.objects.get(id=id)
    y.delete()
    return HttpResponseRedirect('/todoapp/')