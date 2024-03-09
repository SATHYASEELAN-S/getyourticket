from django import forms

from django.contrib.auth.models import User
from user.models import Userprofileinfo
class userFrom(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    # confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=['username','email','password']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
           
        }

class UserprofileinfoForm(forms.ModelForm):
    class Meta():
        model=Userprofileinfo
        fields=['portfolio','profileimage']
    