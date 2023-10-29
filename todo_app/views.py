from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, CreateAPIView, DestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from todo_app.models import Task, Category
from todo_app.permissions import IsOwner
from todo_app.serializers import TaskSerializer, CategorySerializer


# Create your views here.
class TaskViewPagination(PageNumberPagination):
    page_size = 7
    page_size_query_param = 'page_size'
    max_page_size = 100


class TaskView(ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, )
    pagination_class = TaskViewPagination

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskSortedCategoryView(ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, )
    pagination_class = TaskViewPagination

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).filter(category_id=self.kwargs['category_id'])


class TaskSortedCompletedView(ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).filter(completed=True)


class TaskUpdateView(RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsOwner, )


class CreateTaskView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class DeleteTaskView(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsOwner,)


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
