from django.urls import path
from .views import TaskView, TaskUpdateView, CreateTaskView, DeleteTaskView

app_name = 'todo'

urlpatterns = [
    path('<int:pk>/', TaskUpdateView.as_view(), name='update_task'),
    path('', TaskView.as_view(), name='task'),
    path('create/', CreateTaskView.as_view(), name='create_task'),
    path('delete/<int:pk>', DeleteTaskView.as_view(), name='delete_task'),
]
