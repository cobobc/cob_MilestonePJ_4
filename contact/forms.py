from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """ Contact model form that uses all fields except complete """
    class Meta:
        model = Contact
        fields = ['subject', 'name', 'email', 'comments']
