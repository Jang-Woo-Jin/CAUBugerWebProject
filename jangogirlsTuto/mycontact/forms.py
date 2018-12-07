from django import forms

from .models import Contact, MyContact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('title', 'text',)