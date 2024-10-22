from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from django.http import HttpResponse


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Todo App!")
