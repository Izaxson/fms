from fms.models import Received,Sent
from .import forms
from django.forms import ModelForm
    
class ReceivedForm(forms.ModelForm):
    class Meta:
        model = Received
        fields=['subject','file_name','entity','institution','priority','date_received','office_to','county','file','remarks']


class SentForm(forms.ModelForm):
    class Meta:
        model = Sent
        fields=['subject','file_name','sent_to','institution','date_sent','office_from','file','remarks']        
        

        