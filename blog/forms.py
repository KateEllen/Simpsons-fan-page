from django import forms
from .models import Comment
from.models import Characters


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


