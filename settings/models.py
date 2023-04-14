from django.db import models

# Create your models here.
class Company(models.Model):
    name=models.CharField( max_length=100)
    logo=models.ImageField( upload_to='company')
    call_us=models.CharField( max_length=50)
    email_us=models.CharField( max_length=50)
    about=models.TextField(max_length=200)
    fb_link=models.URLField( max_length=200,null=True,blank=True)
    tw_link=models.URLField( max_length=200,null=True,blank=True)
    inst_link=models.URLField( max_length=200,null=True,blank=True)
    emails=models.TextField(max_length=200)
    phones=models.TextField(max_length=200)
    address=models.TextField(max_length=200)
    def __str__(self):
        return self.name