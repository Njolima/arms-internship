from django import forms
from .models import Album


class CreateAlbum(forms.Form):
    # class Meta:
    #     model = Album
    #     fields = '__all__'

    Album_title = forms.CharField(max_length=255)
    genre = forms.CharField(max_length=150)
