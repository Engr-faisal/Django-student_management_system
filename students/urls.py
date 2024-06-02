# students/urls.py

from django.urls import path
from .views import student_create, student_list

urlpatterns = [
    path('create/', student_create, name='student_create'),
    path('', student_list, name='student_list'),
]
