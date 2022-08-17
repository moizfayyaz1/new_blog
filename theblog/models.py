from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    title= models.CharField(max_length=255)
    
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def get_absolute_url(self):
        return reverse('article-detail', args=(str(self.id)))

    def __str__(self):
        return self.title + ' | ' + str(self.author)

class Images(models.Model):
    post= models.ForeignKey(Post,on_delete=models.CASCADE )
    image= models.ImageField(null=True, blank=True)
    

    

class Profile(models.Model):
    user= models.OneToOneField(User, null=True, on_delete= models.CASCADE)
    bio= models.TextField(null=True, blank=True)
    profile_image= models.ImageField(null=True, blank=True, upload_to= 'images/profile/')

    def __str__(self):
        return str(self.user)
