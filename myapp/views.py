from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render

# Create your views here.
def index(request):
    title = "Django Course!"
    return render(request,'index.html', {
        'title': title,
    })

def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2>" % username)

def about(request):
    username = '@juniorpeves'
    return render(request,'about.html',{
        'username': username,
    })

def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request,'projects.html', {
        'projects': projects,
    })

def tasks(request):
    # task = get_object_or_404(Task, id=id)
    return render(request,'tasks.html') 
 