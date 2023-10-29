from django.urls import path
from .views import TaskView, TaskUpdateView, CreateTaskView, DeleteTaskView, TaskSortedCategoryView, TaskSortedCompletedView

app_name = 'todo'

urlpatterns = [
    path('<int:pk>/', TaskUpdateView.as_view(), name='update_task'),
    path('', TaskView.as_view(), name='task'),
    path('create/', CreateTaskView.as_view(), name='create_task'),
    path('delete/<int:pk>', DeleteTaskView.as_view(), name='delete_task'),
    path('sort/category/<int:category_id>/', TaskSortedCategoryView.as_view(), name='sorted_task'),
    path('sort/completed/', TaskSortedCompletedView.as_view(), name='sorted_task'),
]
