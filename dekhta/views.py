from django.shortcuts import render
from django.http import HttpResponse
from .models import Poets, Post
# Create your views here.

def home(request):
    all_posts = Post.objects.all().values()
    poets = Poets.objects.all().values()
    return render(request, 'index.html',{'allposts':all_posts, 'poet':poets})

def all_poets(request):
    poets = Poets.objects.all().order_by('first_name').values()
    return render(request, 'poets.html', {'poet': poets})

def details(request, id):
    poet = Poets.objects.get(id = id)
    all_posts = Post.objects.all().values()
    return render(request, 'details.html', {'poet' : poet, 'posts' : all_posts})

