from django.db import models

# Create your models here.
class BannerArea(models.Model):
    title = models.CharField(max_length=255,db_index=True)
    image = models.ImageField(upload_to='media/contact_banner/')
    
    class Meta:
        verbose_name = "Banner"
        indexes = [models.Index(fields=['title'])]
    
    def __str__(self):
        return self.title
    
                           
class ContactForm(models.Model):
    name = models.CharField(max_length=100,db_index=True)
    email = models.EmailField()
    phone = models.CharField(max_length=150, blank=True, null=True)
    message = models.TextField()
    
    class Meta:
        verbose_name = "Contact Form"
        indexes = [models.Index(fields=['name'])]

    def __str__(self):
        return f"Contact from {self.name}"