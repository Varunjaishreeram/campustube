# In your forms.py file

from django.contrib.auth.forms import AuthenticationForm
from django import forms

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].label = "Email or Username"


class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={
        'rows':'1','placeholder':'add a comment'
    }))
