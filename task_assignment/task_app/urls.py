"""task_assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import CreateEmployee, CreateTask, DeleteTask, CompleteTask,\
    AssignTask, EmployeeTaskView, ViewTaskEmployee, ViewClients, DeleteUser

urlpatterns = [
    # path('employee/create/<str:username>', CreateEmployee.as_view()),
    path('employee/create/', CreateEmployee.as_view()),
    path('view/employees/', ViewTaskEmployee.as_view()),
    path('view/users/', ViewClients.as_view()),
    # path('create/task/<int:task_id>', CreateTask.as_view({'post': 'create', 'get': 'get_one_or_list'})),
    path('create/view/', CreateTask.as_view()),
    # path('view/', CreateTask.as_view({'get': 'get_one_or_list'})),
    path('delete/<int:id>', DeleteTask.as_view()),
    path('delete/user/<int:id>', DeleteUser.as_view()),
    path('complete/<int:id>', CompleteTask.as_view()),
    path('assign/<int:task_id>/<int:user_id>', AssignTask.as_view({'post': 'assign_task'})),
    # path('assign/<int:task_id>/<int:user_id>', AssignTask.as_view()),
    path('employee/<int:id>', EmployeeTaskView.as_view()),
    path('login/', jwt_views.TokenObtainPairView.as_view()),

]
