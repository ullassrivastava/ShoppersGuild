from django import forms


class SignInForm(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField(max_length=10)


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField(max_length=10)
    email = forms.CharField(max_length=20)


class PackAForm(forms.Form):
    packA_tb = forms.CharField(max_length=10)
    packB_tb = forms.CharField(max_length=10)
    packC_tb = forms.CharField(max_length=10)
    QtyA = forms.CharField(max_length=10)
    QtyB = forms.IntegerField()
    QtyC = forms.IntegerField()
