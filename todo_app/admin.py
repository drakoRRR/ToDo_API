from django.contrib import admin

from todo_app.models import Task, Category


# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'posted_date', 'deadline_date', 'completed', 'category', 'user')
    fields = ('id', 'title', 'description', 'posted_date', 'deadline_date', 'completed', 'category', 'user')
    readonly_fields = ('id', 'posted_date', 'deadline_date')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    fields = ('id', 'name')
