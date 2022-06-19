"""Register your models here."""
from django.contrib import admin
from .models import DefineTasks, AssignTaskToEmployee


admin.site.register(DefineTasks)
admin.site.register(AssignTaskToEmployee)
