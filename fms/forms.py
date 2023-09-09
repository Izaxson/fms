from fms.models import Received,Sent
from .import forms
from django.forms import ModelForm

from django import forms
    
class ReceivedForm(forms.ModelForm):
    class Meta:
        model = Received
        fields=['subject','file_name','entity','institution','priority','date_received','office_to','county','file','remarks']


class UpdateReceivedForm(forms.ModelForm):
    class Meta:
        model = Received
        fields = ['subject', 'file_name', 'entity', 'institution', 'priority', 'date_received', 'office_to', 'county', 'file', 'remarks']

    # Define widgets for each field
    widgets = {
        'subject': forms.TextInput(attrs={'class': 'form-control'}),
        'file_name': forms.TextInput(attrs={'class': 'form-control'}),
        'entity': forms.TextInput(attrs={'class': 'form-control'}),
        'institution': forms.TextInput(attrs={'class': 'form-control'}),
        'priority': forms.TextInput(attrs={'class': 'form-control'}),
        'date_received': forms.DateInput(attrs={'class': 'form-control'}),
        'office_to': forms.TextInput(attrs={'class': 'form-control'}),
        'county': forms.TextInput(attrs={'class': 'form-control'}),
        'file': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),  # ClearableFileInput for file fields
        'remarks': forms.Textarea(attrs={'class': 'form-control'}),
    }

class SentForm(forms.ModelForm):
    class Meta:
        model = Sent
        fields=['subject','file_name','sent_to','institution','date_sent','office_from','file','remarks']        
        
class UpdateSentForm(forms.ModelForm):
    class Meta:
        model = Sent
        fields = ['subject', 'file_name', 'sent_to', 'institution', 'date_sent', 'office_from', 'file', 'remarks']

    subject = forms.CharField(
        label='Subject',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=255,
        required=True,
    )

    file_name = forms.CharField(
        label='File Name',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=255,
        required=True,
    )

    sent_to = forms.CharField(
        label='Sent To',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=255,
        required=True,
    )

    institution = forms.CharField(
        label='Institution',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=255,
        required=True,
    )

    date_sent = forms.DateField(
        label='Date Sent',
        widget=forms.DateInput(attrs={'class': 'form-control'}),
        required=True,
    )

    office_from = forms.CharField(
        label='Office From',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=255,
        required=True,
    )

    file = forms.FileField(
        label='File',
        required=True,  # Depending on your requirements, this field can be optional
    )

    remarks = forms.CharField(
        label='Remarks',
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        required=False,  # Depending on your requirements, this field can be optional
    )
        