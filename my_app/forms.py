from typing import Text
from django import forms
from .models import AudioFile


class AudioForm(forms.ModelForm): #we use modelform coz we linking this with model
    name = forms.CharField(max_length=25, required=True, widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "Enter name"}))
    audio = forms.FileField(required=True, widget=forms.FileInput(
        attrs={'class': "form-control", 'placeholder': "Audio"}))
    class Meta:
        model = AudioFile
        fields = ["name", "audio"]
