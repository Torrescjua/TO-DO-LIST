from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    """
    A model representing a task with a title, description, status, and associated user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['done', '-created']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        constraints = [
            models.UniqueConstraint(fields=['user', 'title'], name='unique_task_per_user')
        ]

    def mark_as_done(self):
        """
        Mark the task as done.
        """
        self.done = True
        self.save()

    def mark_as_pending(self):
        """
        Mark the task as pending.
        """
        self.done = False
        self.save()
