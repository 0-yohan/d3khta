from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Poets, Post
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import NewUserForm
# Create your views here.

def home(request):
    all_posts = Post.objects.all().order_by('-id')[:5].values()
    poets = Poets.objects.all().values()
    return render(request, 'index.html',{'allposts':all_posts, 'poet':poets})

def all_poets(request):
    poets = Poets.objects.all().order_by('first_name').values()
    return render(request, 'poets.html', {'poet': poets})

def details(request, id):
    poet = Poets.objects.get(id = id)
    all_posts = Post.objects.all().values()
    return render(request, 'details.html', {'poet' : poet, 'posts' : all_posts})

def create_user(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(f"User Created")

            return redirect('login/')

    else:
        form = NewUserForm()
        
    return render(request, 'create_user.html', {'form' : form})
    

        

