from django import forms
from blog.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'content', 'author', 'category', 'is_published', 'tags', 'image', 'created_at', 'updated_at')

        widgets = {
            'title' : forms.forms.TextInput(attrs={'class': 'form-control custom-text-input'}),
            'slug' : forms.forms.TextInput(attrs={'class': 'form-control custom-slug-input'}),
            'content' : forms.forms.Textarea(attrs={'class': 'form-control custom-textarea'}),
            'is_published' : forms.forms.CheckboxInput(attrs={'class': 'form-control custom-checkbox'}),
            'image' : forms.forms.ClearableFileInput(attrs={'class': 'form-control custom-image-input'}),
            'created_at' : forms.forms.DateTimeInput(attrs={'class': 'form-control datetimepicker'}),
            'updated_at' : forms.forms.DateTimeInput(attrs={'class': 'form-control datetimepicker'}),
        }
