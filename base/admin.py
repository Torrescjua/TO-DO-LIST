from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    """
    Custom admin class for the Task model.
    """
    list_display = ('title', 'user', 'done', 'created')
    list_filter = ('done', 'created')
    search_fields = ('title', 'description', 'user__username')
    ordering = ('-created', 'done')

# Register your models here.
admin.site.register(Task, TaskAdmin)
