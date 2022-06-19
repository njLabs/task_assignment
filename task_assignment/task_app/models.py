"""Create model for task assignment."""
from django.db import models
from django.contrib.auth.models import User


class DefineTasks(models.Model):
    """define task with auto datetime fields."""
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    task = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AssignTaskToEmployee(models.Model):
    """assign tasks to employees with auto datetime field."""
    task = models.ForeignKey(DefineTasks, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
