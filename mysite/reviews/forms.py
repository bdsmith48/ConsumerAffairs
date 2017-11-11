from django import forms
from . import models

class WriteReviewForm(forms.Form):
    title = forms.CharField(label = "Title", max_length = 64)
    summary = forms.CharField(label = "Summary", max_length = 10000)
    company = forms.CharField(label = "What company is this for?", max_length = 30)
    rating = forms.IntegerField(label = "Rating", min_value = 0, max_value = 5)
