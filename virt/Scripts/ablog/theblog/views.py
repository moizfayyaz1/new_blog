from audioop import reverse
from django.contrib import messages
from http.client import HTTPResponse
from pdb import post_mortem
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Images
from .forms import ImageForm, PostForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect 
# def home(request):
#    return render(request, 'home.html',{})

class HomeView(ListView):
    model= Post
    template_name= 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name= 'article_details.html'

def AddPostView(request):
    model= Images
    if request.method == "POST":
        form= PostForm(request.POST)
        files = request.FILES.getlist("Images")
        if form.is_valid():
            f=form.save(commit=False)
            f.user=request.user
            f.save()
            for i in files:
                Images.objects.create(post=f, Images= i)
            messages.success(request, "New Blog added")
            return HttpResponseRedirect("/")
    else:
        form= PostForm()
        imageform= ImageForm()

    return render (request, "add_post.html",{"form":form,"imageform":imageform})


class UpdatePostView(UpdateView):
    model= Post
    template_name= 'update_post.html'
    fields= ['title','body']

class DeletePostView(DeleteView):
    model= Post
    template_name= 'delete_post.html'
    success_url = reverse_lazy('home')
