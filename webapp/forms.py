from django import forms
from webapp.models import Post

class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')