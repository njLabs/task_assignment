from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from .models import DefineTasks, AssignTaskToEmployee


class TaskSerializer(ModelSerializer):
    """DefineTasks serializer"""
    class Meta:
        model = DefineTasks
        fields = "__all__"
        required_field_names = None



class UserSerializer(ModelSerializer):
    """user model serializer"""
    class Meta:
        model = User
        fields = "__all__"


class EmployeeTaskSerial(ModelSerializer):
    """AssignTaskToEmployee serializer"""
    assigned_to = UserSerializer()
    task = TaskSerializer()
    class Meta:
        model = AssignTaskToEmployee
        fields = "__all__"





