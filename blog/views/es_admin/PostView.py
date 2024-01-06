from blog.models import Post
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from blog.forms.PostForm import PostForm

def index(request):
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 8)
    page = request.GET.get('page', 1)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except:
        posts = paginator.page(1)

    return render(request, 'blog/posts/post_index.html', {'posts': posts})

# Les autres fonctions comme show, create, update, delete... 
def show(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/posts/post_show.html', {'post': post})

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post has been saved !')
            return redirect('post_index')
    else:
        form = PostForm()
    return render(request, 'blog/posts/post_new.html', {'form': form})

def update(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        if request.POST.get('_method') == 'PUT':
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                messages.success(request, 'Post has been updated !')
                return redirect('post_index')
        else:
            form = PostForm(instance=post)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/posts/post_new.html', {'form': form, 'post': post})

def delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        if request.POST.get('_method') == 'DELETE':
            post.delete()
            messages.success(request, 'Post has been deleted !')
    return redirect('post_index')

