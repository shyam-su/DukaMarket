from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255,db_index=True)
    address = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=20,db_index=True)
    logo = models.ImageField(upload_to='company/logos/', blank=True)
    address_url = models.URLField(null=True, blank=True)
    
    
    class Meta:
        verbose_name = "Company"
        indexes = [models.Index(fields=['name','phone_number'])]


    def __str__(self):
        return self.name
    
class FooterWidget(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    
    class Meta:
        verbose_name = "Footer Widget"
        indexes = [models.Index(fields=['title'])]
    

class SocialMediaLink(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    icon = models.CharField(max_length=100) 
    
    class Meta:
        verbose_name = "Social Media Link"
        indexes = [models.Index(fields=['name'])]

    def __str__(self):
        return self.name

class CustomerService(models.Model):
    title = models.CharField(max_length=100,db_index=True)
    url = models.URLField()
    
    class Meta:
        verbose_name = "Customer Service"
        indexes = [models.Index(fields=['title'])]

    def __str__(self):
        return self.title

class Download_App(models.Model):
    name=models.CharField(max_length=100,db_index=True)
    link=models.CharField(max_length=100,default=False)
    image=models.ImageField(upload_to='media/download_app/')
    
    
    class Meta:
        verbose_name = "Download App"
        indexes = [models.Index(fields=['name'])]
