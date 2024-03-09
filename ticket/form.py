from django import forms

from ticket.models import BusInfo,Stop

class BusInfoForm(forms.ModelForm):
    class Meta:
        model=BusInfo
        exclude=['user']

    
class StopForm(forms.ModelForm):
    class Meta:
        model=Stop
        exclude=['bus_no']

