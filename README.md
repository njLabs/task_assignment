# Task Management API

This project is a simple task management API built with Django REST Framework (DRF) using generic API views and JWT authentication. It defines three roles: Manager, Employee, and Client, with specific permissions for each. The application uses MySQL as the database backend.

## Features

- **Roles**:
  - **Client**: Can create tasks.
  - **Manager**: Can delete tasks and assign tasks to Employees.
  - **Employee**: Can mark tasks as complete.

- **Endpoints**:
  - Task Management:
    - Create Task
    - Edit Task
    - Delete Task
    - Assign Task
    - Complete Task
  - Authentication:
    - User Login (JWT-based)
    - User Logout
  
## Tech Stack

- Python 3
- Django & Django REST Framework
- MySQL
- JWT Authentication

## Installation

### Prerequisites

- Python 3.8 or higher
- MySQL Server

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/njLabs/task_assignment.git
   cd task-management-api
