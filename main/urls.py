from django.urls import path

from main.views import HomeView, CreateToDoView, ToDoView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add-todo', CreateToDoView.as_view(), name='create'),
    path('mytodo', ToDoView.as_view(), name='mytodo'),
]