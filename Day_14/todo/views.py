from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import *
from .forms import *

def index(request):
    tasks = Task.objects.all()
    forms = TaskForm()
    if request.method == 'POST':
       forms = TaskForm(request.POST)
       if forms.is_valid():
            forms.save()
       return redirect('/')
    context = {'tasks': tasks, 'forms': forms}
    return render(request, 'list.html', context)