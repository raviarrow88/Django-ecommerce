from django.db import models
from baseapp.models.timestamp import TimeStamp
from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from allauth.socialaccount.signals import social_account_added

class UserProfile(TimeStamp):

    """
    This model is an extension of the User model that is inbuilt in django.
    It is connected to django User model with a OneToOneField.
    """
    user = models.OneToOneField(User,related_name='user',on_delete=models.CASCADE)
    avatar = models.URLField(max_length=100,blank=True,null=True)
    phone_regex = RegexValidator(regex=r'^\+?([0,7,8,9]{1})}?\d{9,12}$',
                                 message="Phone number must be entered in the format: '9848281223'. Up to 11 digits allowed.")

    phone_number = models.CharField(validators=[phone_regex],max_length=10,verbose_name='User phone number',null=True,blank=True)

    fb_profile = models.URLField(max_length=255,null=True,blank=True,default=None)
    gmail_profile = models.URLField(max_length=255,null=True,blank=True,default=None)



    def __str__(self):
        return str(self.id)



@receiver(user_signed_up)
def create_user_profile(request,user,sociallogin=None,**kwargs):
    if sociallogin:
        new_user = User.objects.get(email=user.email)
        avatar_url = sociallogin.account.get_avatar_url()
        user_profile,created = UserProfile.objects.get_or_create(user=new_user,avatar=avatar_url)
        if sociallogin.account.provider =='google':
            new_user = User.objects.filter(email=user.email)[0]
            profile = UserProfile.objects.filter(user=new_user)[0]
            profile.gmail_profile = sociallogin.account.get_profile_url()
            profile.save()
        elif sociallogin.account.provider =='facebook':
            new_user = User.objects.filter(email=user.email)[0]
            profile = UserProfile.objects.filter(user=new_user)[0]
            print ("url",sociallogin.account.get_profile_url())
            profile.fb_profile = sociallogin.account.get_profile_url()
            profile.save()
