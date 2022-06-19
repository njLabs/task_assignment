"""logic view of task assignment"""
from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .models import DefineTasks, AssignTaskToEmployee
from .permissions import IsManager, IsClient, IsEmployee
from .serializers import UserSerializer, TaskSerializer, EmployeeTaskSerial


class CreateEmployee(generics.CreateAPIView, generics.ListCreateAPIView, generics.RetrieveAPIView):
    permission_classes = [IsClient, ]
    queryset = User
    serializer_class = UserSerializer
    lookup_field = 'id'

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'status': 200,
            'message': 'Employee successfully created.',
            'data': response.data
        })


class ViewClients(generics.ListCreateAPIView):
    """view end users"""
    permission_classes = [IsManager, ]
    queryset = User.objects.filter(is_superuser=False, is_staff=True)
    serializer_class = UserSerializer


class CreateTask(generics.CreateAPIView, generics.ListCreateAPIView):
    permission_classes = [IsClient, ]
    queryset = DefineTasks.objects.all()
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'status': 200,
            'message': 'Employee successfully created.',
            'data': response.data
        })


class DeleteTask(generics.DestroyAPIView):
    """delete task using task_id"""
    permission_classes = [IsManager, ]
    queryset = DefineTasks.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'

    # def delete_task(self, request, task_id):
    #     global context
    #     task = get_object_or_404(DefineTasks, pk=task_id)
    #     task.delete()
    #     context = {"message": "Task deleted"}
    #     return Response(context, status=200)


class DeleteUser(generics.DestroyAPIView):
    """delete task using task_id"""
    permission_classes = [IsManager, ]
    queryset = User
    serializer_class = UserSerializer
    lookup_field = 'id'
    # def delete_user(self, request, user_id):
    #     global context
    #     task = get_object_or_404(User, pk=user_id)
    #     task.delete()
    #     context = {"message": "User deleted"}
    #     return Response(context, status=200)


class CompleteTask(generics.UpdateAPIView):
    """
    use patch method to update the task using
    is_completed=true
    """
    permission_classes = [IsEmployee, ]
    queryset = DefineTasks.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'


class EmployeeTaskView(generics.RetrieveAPIView):
    """return employees tasks view"""
    permission_classes = [IsEmployee, ]
    queryset = AssignTaskToEmployee.objects.all()
    serializer_class = EmployeeTaskSerial
    lookup_field = 'id'


class AssignTask(viewsets.ViewSet):
    """assign task to user using their respective user_id"""
    permission_classes = [IsManager, ]
    def assign_task(self, request, task_id, user_id):
        print(task_id, user_id)
        user_obj = get_object_or_404(User, pk=user_id)
        task_obj = get_object_or_404(DefineTasks, pk=task_id)
        assign_task_to_employee = AssignTaskToEmployee.objects.create(assigned_to=user_obj, task=task_obj)
        if assign_task_to_employee:
            return Response({"message": f"Task id: {task_id} is assigned to user id: {user_id}"}, status=200)


class ViewTaskEmployee(generics.ListCreateAPIView):
    """returns list of employees"""
    permission_classes = [IsManager, ]
    queryset = User.objects.filter(is_superuser=False, is_staff=False)
    serializer_class = UserSerializer
