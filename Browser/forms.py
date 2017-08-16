from django import forms


class SignInForm(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField(max_length=10)


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField(max_length=10)
    email = forms.CharField(max_length=20)
