from django.urls import path
from todoapp import views
urlpatterns = [
    path('employees/',views.index, name='index'),
    path('employees/<int:pk>/', views.employee_detail, name='employee_detail')
]
