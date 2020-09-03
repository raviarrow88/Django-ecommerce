from django import forms
from .models.contact import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields=('name','phone_number','email','message')


from .models.address import Address
class AddressForm(forms.ModelForm):
    name = forms.CharField()
    email = forms.CharField()
    class Meta:
        model=Address
        fields = ('title','name','email','street_address','city','state','zip')
