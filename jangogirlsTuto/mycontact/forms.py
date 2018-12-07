from django import forms

from .models import User

class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('userId', 'userPw')

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('userName', 'userId', 'userPw')

class SearchPWForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('userId',)

class ChangePWForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('userPw',)

