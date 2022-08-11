from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy
# def home(request):
#    return render(request, 'home.html',{})

class HomeView(ListView):
    model= Post
    template_name= 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name= 'article_details.html'

class AddPostView(CreateView):
    model= Post
    form_class= PostForm
    template_name= 'add_post.html'
    #fields= ('title','body')

class UpdatePostView(UpdateView):
    model= Post
    template_name= 'update_post.html'
    fields= ['title','body']

class DeletePostView(DeleteView):
    model= Post
    template_name= 'delete_post.html'
    success_url = reverse_lazy('home')
