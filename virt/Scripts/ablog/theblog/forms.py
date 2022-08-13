from django import forms
from .models import Images, Post

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = ('title', 'body','author')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'})
        }

class ImageForm(forms.ModelForm):
    
    image= forms.ImageField(
        label="Image",
        widget= forms.ClearableFileInput(attrs={"multiple":True}),
        )

    class Meta:
        model= Images
        fields= ("image",)
