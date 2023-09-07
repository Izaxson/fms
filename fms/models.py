from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    is_governor=models.BooleanField(default=False)
    is_deputy_governor=models.BooleanField(default=False)
    is_clerk=models.BooleanField(default=True)
    profile_pic= models.ImageField(upload_to='profiles/', validators=[FileExtensionValidator(['jpeg','jpg','gif', 'png'])])

    def __str__(self):
        return self.user.username
    
class Received(models.Model):
   
    OFFICE_TO = (
        ('Office_of_The_Governor', 'Office of The Governor'),
        ('Office_of_The_Deputy_Governor', 'Office of The Deputy Governor')
    )

    Government = (
        ('National', 'National'),
        ('County', 'County'),
        ('Other', 'Other')
    )
    Priority = (
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low')
    )

    County = (
        ('Mandera_County', 'Mandera County'),
        ('Wajir_County', 'Wajir County'),
        ('Garissa_County', 'Garissa County')
    )
    subject=models.CharField(max_length=100)
    file_name = models.CharField(max_length=100)
    entity=models.CharField(choices=Government,max_length=150)
    institution = models.CharField(max_length=100)
    priority=models.CharField(choices=Priority,max_length=150)
    date_received = models.DateField()
    office_to= models.CharField(choices=OFFICE_TO, max_length=200)
    county=models.CharField(choices=County,max_length=150,blank=True,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='files/', validators=[FileExtensionValidator(['pdf', 'docx', 'doc', 'xls', 'xlsx', 'ppt', 'pptx'])])
    remarks = models.TextField(max_length=100,null=True,blank=True)
    class  Meta:
        ordering=['-id']
        verbose_name = 'Received'
        verbose_name_plural = 'Received'

    def __str__(self):
        return self.subject
    
class Sent(models.Model):
   
    OFFICE_FROM = (
        ('Office_of_The_Governor', 'Office of The Governor'),
        ('Office_of_The_Deputy_Governor', 'Office of The Deputy Governor')
    )

    Government = (
        ('National', 'National'),
        ('County', 'County'),
        ('Other', 'Other')
    )

    County = (
        ('Mandera_County', 'Mandera County'),
        ('Wajir_County', 'Wajir County'),
        ('Garissa_County', 'Garissa County')
    ) 
    subject=models.CharField(max_length=100)
    file_name = models.CharField(max_length=100)
    sent_to=models.CharField(choices=Government,max_length=150)
    institution = models.CharField(max_length=100)
    date_sent = models.DateField()
    office_from= models.CharField(choices=OFFICE_FROM, max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='files/', validators=[FileExtensionValidator(['pdf', 'docx', 'doc', 'xls', 'xlsx', 'ppt', 'pptx'])])
    remarks = models.TextField(max_length=100,null=True,blank=True)

    class Meta:
        verbose_name = 'Sent'
        verbose_name_plural = 'Sent'
        
    
    def __str__(self):
        return self.subject