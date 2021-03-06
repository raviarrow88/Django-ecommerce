from django import forms
from .models.contact import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields=('name','phone_number','email','message')


from .models.address import Address
class AddressForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model=Address
        fields = ('name','phone_number','street_address','apartment_address','city','state','zip',)

    # def __init__(self,*args,**kwargs):
    #     super(AddressForm,self).__init__(*args,**kwargs)
    #
    #     self.fields['email'].disabled=True
