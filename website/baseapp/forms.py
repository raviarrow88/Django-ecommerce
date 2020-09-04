from django import forms
from .models.contact import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields=('name','phone_number','email','message')


from .models.address import Address
class AddressForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Eg:Home/Office'}))
    name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model=Address
        fields = ('title','name','phone_number','street_address','apartment_address','city','state','zip','email')

    def __init__(self,*args,**kwargs):
        super(AddressForm,self).__init__(*args,**kwargs)

        self.fields['email'].disabled=True
