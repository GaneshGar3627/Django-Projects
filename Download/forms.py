from django import forms


class Ddownload(forms.Form):
    title = forms.URLField()
