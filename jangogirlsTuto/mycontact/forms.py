from django import forms

from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', 'password')

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class SearchPWForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)

class ChangePWForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('password',)

