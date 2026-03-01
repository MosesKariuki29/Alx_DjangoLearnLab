from django import forms

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()

class BookSearchForm(forms.Form):
    q = forms.CharField(max_length=100, required=False)