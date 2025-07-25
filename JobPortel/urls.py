
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.Employee_from_view, name='upload'),  # For creating
    path('change/<int:id>/', views.Employee_change_list, name='change'),  # For editing
    path('sum/', views.Employees_list, name='list'),  # List employees
    path('delete/<int:id>/', views.Employee_delete_list, name='delete'),  # Delete
]
