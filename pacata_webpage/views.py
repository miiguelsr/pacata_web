from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class PostView(DetailView):
    model = Post
    template_name = 'post_view.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'