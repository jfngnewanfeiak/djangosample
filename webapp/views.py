from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from webapp.models import Post
from .forms import PostCreateForm
# Create your views here.

class PostListView(generic.ListView):
    model = Post

class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('webapp:post_list')

class PostDetailView(generic.DetailView):
    model = Post

class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = reverse_lazy('webapp:post_detail')

class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('webapp:post_list')