from django import forms


class RegistrationForm(forms.Form):
    email = forms.EmailField()
    username = forms.CharField(min_length=1, max_length=30)
    password = forms.CharField(min_length=5, max_length=30)
    firstname = forms.CharField(min_length=1, max_length=30)
    lastname = forms.CharField(min_length=1, max_length=30)

class CreateTask(forms.Form):
    name = forms.CharField()
    desc = forms.CharField(widget=forms.Textarea)
    dateFinishAdmin = forms.DateField()