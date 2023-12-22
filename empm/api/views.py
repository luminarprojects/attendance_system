from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, EmployeeSerializer
from django.contrib.auth.models import User
from .models import Employee


class EmployeeCreateView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            # Extract user data from request
            user_data = {
                "username": request.data.get('username'),
                "password": request.data.get('password')
            }

            # Create User
            user_serializer = UserSerializer(data=user_data)
            user_serializer.is_valid(raise_exception=True)
            user = user_serializer.save()

            # Continue with the Employee creation
            employee_data = request.data.copy()
            employee_data['user'] = user.id

            employee_serializer = EmployeeSerializer(data=employee_data)
            employee_serializer.is_valid(raise_exception=True)
            employee_serializer.save()

            return Response(employee_serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class EmployeeListView(APIView):
    def get(self, request, *args, **kwargs):
        employees = Employee.objects.all()
        serialized_data = []

        for employee in employees:
            employee_data = EmployeeSerializer(employee).data
            user_data = employee.user  # Access the user data from the employee instance
            employee_data['user'] = {
                'id': user_data.id,
                'username': user_data.username,
                'email': user_data.email  # Add other user fields as needed
            }
            serialized_data.append(employee_data)

        return Response(serialized_data)


# views.py
from django.shortcuts import render
from django.views.generic import DetailView

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee_detail.html'  # Replace with the actual template name for employee detail

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # You can add additional context data if needed
        return context







# {

#         "username": "example_user",
#         "password": "example_password"
#     "employee_id": "12345",
#     "name": "John Doe",
#     "department": "IT",
#     "designation": "back-end developer",
#     "phone": "123-456-7890",
#     "mail": "john.doe@example.com",
#     "jobmethod": "office"
# }
