from django import forms
from .models.contact import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields=('name','phone_number','email','message')
