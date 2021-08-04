from django import forms

from api.models import NewsLetter

class PostForm(forms.ModelForm):

    class Meta:
        model = NewsLetter
        fields = ('nome', 'email',)