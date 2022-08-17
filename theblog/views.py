from audioop import reverse
from django.contrib import messages
from http.client import HTTPResponse
from pdb import post_mortem
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
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
    
      

def ArticleDetailView(request, id):

    post = Post.objects.get(id=id)
    print(post.images_set.all())
    return render(request, 'article_details.html', {'post':post,})

def AddPostView(request):
    if request.method == 'POST':
        
        p = Post(
            title=request.POST.get('postTitle'),
            body=request.POST.get('description'),   
            author= request.POST.get('author'),         
        )
        p.save()
      
        
        for afile in request.FILES.getlist('postImg'):
            img = Images(post=p,
                                image=afile,
                                )
            img.save()
            check=False
        return redirect('home')

    
    return render(request, 'add_post.html')

class UpdatePostView(UpdateView):
    model= Post
    template_name= 'update_post.html'
    fields= ['title','body']

class DeletePostView(DeleteView):
    model= Post
    template_name= 'delete_post.html'
    success_url = reverse_lazy('home')
