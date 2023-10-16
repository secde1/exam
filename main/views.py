from django.shortcuts import render
from django.template.context_processors import request


def HomeView(View): # noqa
    return render(request, "index.html")


