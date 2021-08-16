from django import forms
from .models import Comment, Post

class NewCommentForm(forms.ModelForm):
    """ For for use to add a comment to blog post """
    class Meta:
        model = Comment
        fields = ("name", "email", "content")
        widgets = {
            "name": forms.TextInput(attrs={"class": "col-sm-12"}),
            "email": forms.TextInput(attrs={"class": "col-sm-12"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
        }

class PostSearchForm(forms.Form):
    q = forms.CharField()
    