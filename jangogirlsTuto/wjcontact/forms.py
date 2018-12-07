from django import forms

from .models import WJContact

class ContactForm(forms.ModelForm):

    class Meta:
        model = WJContact
        fields = ('author', 'name','phone_number', 'e_mail_address', 'detail',)