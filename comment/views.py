from django.shortcuts import render
from comment.models import Comment

def comment(request):
    return render(request, 'home.html')

