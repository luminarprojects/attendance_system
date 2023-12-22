
from django.urls import path
from . import views


urlpatterns = [

    path('employee/create',views.EmployeeCreateView.as_view(),name='emp-create'),
    path('employee/list', views.EmployeeListView.as_view(),name='emp-list'),
   
]