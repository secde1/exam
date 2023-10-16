from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.db.models import Q

from .models import ToDo


class HomeView(View):
    template_name = 'index.html'
    context = {}

    def get(self, request):
        return render(request, self.template_name)


class ToDoView(View):
    template_name = 'to_do.html'
    context = {}

    def get(self, request):
        user = request.user
        products = ToDo.objects.filter(user=user)
        self.context.update({'products': products})
        return render(request, self.template_name, self.context)

    def post(self, request):
        id = request.POST.get('id')
        user = request.user
        todo = ToDo.objects.get(Q(id=id) & Q(user=user))
        todo.delete()
        return redirect('/to-do')




class CreateToDoView(View):
    template_name = 'add-todo.html'
    context = {}

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):

        name = request.POST.get('ToDo_Name')
        expires_at = request.POST.get('expires_at')
        user = request.user


        todo = ToDo.objects.create(
            text=name,
            expires_at=expires_at,
            user=user
        )

        todo.save()
        messages.success(request, 'ToDo created successfully')
        return redirect('/add-todo')