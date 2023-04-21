from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Poets, Post, Queries
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
# Create your views here.

def home(request):
    all_posts = Post.objects.all().order_by('-id')[:4].values()
    poets = Poets.objects.all().values()
    return render(request, 'index.html',{'allposts':all_posts, 'poet':poets})

def all_poets(request):
    poets = Poets.objects.all().order_by('first_name')
    poets = poets[1:]
    return render(request, 'poets.html', {'poet': poets})

def details(request, first_name, last_name):
    poet = Poets.objects.get(first_name= first_name, last_name = last_name)
    all_posts = Post.objects.all().values()
    context = {'poet' : poet, 'posts' : all_posts, 'show_add_post_button' : False}
    if (request.user == poet.user):
        context['show_add_post_button'] = True
    return render(request, 'details.html', context)

def create_user(request):
    if request.method == 'POST' and request.user.is_superuser:
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"User Created")
            return redirect('login')
    else:
        form = NewUserForm()
    return render(request, 'create_user.html', {'form' : form})
    
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        data = request.POST['data']
        query = Queries(name = name, email=email, msg=data)
        query.save()

        return redirect('queries')

    else:
        return render(request, 'contact.html')

 

def read(request):
    all_posts = Post.objects.all().values()
    poets = Poets.objects.all().values()
    return render(request, 'read.html',{'allposts':all_posts, 'poet':poets})

def post_detail(request, post_id):
    post = Post.objects.get(id = post_id)
    context = {'post': post, 'show_delete':False}
    if request.user.is_authenticated and hasattr(request.user, 'poets') and request.user.poets.id == post.poet_id_id:
        context['show_delete'] = True

    return render(request, 'post_detail.html', context)

def queries(request):
    query = Queries.objects.all().order_by('id').values()
    return render(request, 'queries.html', {'query':query})


@login_required
def add_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['data']
        time = datetime.now()
        poet_id = request.user.poets.id  
        poem = Post(title=title, data=content, d_time=time, poet_id_id=poet_id)
        poem.save()
    
        poet = Poets.objects.get(id=poet_id)
        poet.posts_count += 1
        poet.save()
        return redirect('read')  

    else:
        return render(request, 'editor.html') 

@login_required      
def delete_post(request, post_id):
    post = Post.objects.get(id = post_id)
    poet = Poets.objects.get(id = post.poet_id_id)

    if request.method=='POST':

        if request.user.is_authenticated and request.user.poets.id == post.poet_id_id:
            post.delete()
            messages.success(request, 'Post deleted')
            poet.posts_count -= 1
            poet.save()
            return redirect('read')
        
        else:
            messages.error(request, 'You donot have permission to delete this post! %s %s' %(poet.id, poet2.id))
            return redirect('post_detail', post_id = post_id)
    
    else:
        return redirect('post_detail', post_id = post_id)



