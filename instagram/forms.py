from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # all 로 했더니 , author 까지 재지정됨 
        # 특정 Fields 만 작성할 수 있도록 변경 
        fields = ["photo", "caption", "location"]
        widgets = {
            "caption" : forms.Textarea,
            
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']