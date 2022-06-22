from django import forms

class PersonForm(forms.Form):
    name = forms.CharField(max_length=50, required=False)
    age = forms.IntegerField(required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(max_length=150, required=False)
