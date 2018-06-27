from django import forms


class CountryForm(forms.Form):
    name = forms.CharField(max_length=128)
