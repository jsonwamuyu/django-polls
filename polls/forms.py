from django import forms

class ContactMeForm(forms.Form):
    fullname = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)