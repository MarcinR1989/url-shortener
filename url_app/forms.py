from django import forms


class UrlForm(forms.Form):
    url = forms.CharField(label='Type your URL', max_length=256)
