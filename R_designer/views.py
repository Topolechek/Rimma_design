from django.shortcuts import render
from my_projects.models import Project
from comment.models import Comment

def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects':projects})


def home(request):
    comments = Comment.objects.all()
    return render(request, 'home.html', {'comments':comments})