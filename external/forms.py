"""Imagetext Forms."""
from django import forms

class ImageForm(forms.Form):
    image = forms.ImageField()
    model_type = forms.TextField()
    beam_index = forms.IntegerField()