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

def details(request, first_name, last_name):
    poet = Poets.objects.get(first_name= first_name, last_name = last_name)
    all_posts = Post.objects.all().values()
    context = {'poet' : poet, 'posts' : all_posts, 'show_add_post_button' : False}
    if (request.user == poet.user):
        context['show_add_post_button'] = True
    return render(request, 'details.html', context)

def create_user(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"User Created")
            return redirect('login')
    else:
        form = NewUserForm()
    return render(request, 'create_user.html', {'form' : form})
    
def contact(request):
    
    return render(request, 'contact.html')

        

