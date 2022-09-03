from django.shortcuts import render

from users.models import User


def home(request):
    users = User.objects.all()
    return render(request, 'index.html',
                  context={'users': users})


def about(request):
    return render(request, 'about.html')
