from django.shortcuts import render
from .models import Blog

def home(request):
    objects = Blog.objects
    return render(request, 'home.html', {'inform':objects})
# Create your views here.
