from django import forms

from .models import bitly

class bitlyForm(forms.ModelForm):
    class Meta:
        model = bitly
        fields = ['long_url']


class editBitly(forms.ModelForm):
    class Meta:
        model = bitly
        fields = ["long_url", "shortcode"]