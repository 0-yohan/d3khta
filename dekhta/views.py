from django.shortcuts import render
from django.http import HttpResponse
from .models import Poets, Post
# Create your views here.

def home(request):
    all_posts = Post.objects.all().order_by('-id').values()
    poets = Poets.objects.all().values()
    return render(request, 'index.html',{'allposts':all_posts, 'poet':poets})
