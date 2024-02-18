from django.http import HttpResponse, JsonResponse
from .models import Project, Task

# Create your views here.
def index(request):
    return HttpResponse("<h2>Index page</h2>")

def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2>" % username)

def about(request):
    return HttpResponse("<h2>About</h2>")

def projects(request):
    projects = Project.objects.all()
    return JsonResponse(projects)

def tasks(request):
    return HttpResponse("tasks")
