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
    """ Form Text input for post search """
    q = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['q'].label = 'Search For'
        self.fields['q'].widget.attrs.update(
            {'class': 'form-control'})
