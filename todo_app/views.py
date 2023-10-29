from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAdminUser

from todo_app.models import Task, Category
from todo_app.permissions import IsOwnerOrReadOnly
from todo_app.serializers import TaskSerializer, CategorySerializer


# Create your views here.
class TaskView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskUpdateView(RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class CreateTaskView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class DeleteTaskView(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUser, )


# class TaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#
#
# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = (IsAdminUser, )
