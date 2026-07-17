from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    Provides full CRUD automatically:
    GET    /api/tasks/        -> list all tasks
    POST   /api/tasks/        -> create a task
    GET    /api/tasks/<id>/   -> get one task
    PUT    /api/tasks/<id>/   -> update a task fully
    PATCH  /api/tasks/<id>/   -> update a task partially (e.g. just status)
    DELETE /api/tasks/<id>/   -> delete a task
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
