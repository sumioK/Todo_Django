from django.urls import path, include
from .view import TodoList

urlpatterns = [
    path('list/', TodoList.as_view()),
]
