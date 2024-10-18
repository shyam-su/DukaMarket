from django.db import models
from shop.models import *

# Create your models here.
class Navbar_text(models.Model):
    text=models.CharField(max_length=100,db_index=True)
    logo=models.ImageField(upload_to='media/nav_logo/',null=True, blank=True,db_index=True)
    
    class Meta:
        verbose_name = "Navbar"
        indexes = [models.Index(fields=['text'])]
    
    def __str__(self):
        return self.text
    
class Deals(models.Model):
    DISCOUNT_DEAL_CHOICES = (
        ('HOT SALE', 'HOT SALE'),
        ('NEW ARRIVALS', 'NEW ARRIVALS'),
        ('ON SALE', 'ON SALE'),
    )

    # Define the field with choices and a maximum length
    delas = models.CharField(choices=DISCOUNT_DEAL_CHOICES, max_length=100)
    
    class Meta:
        verbose_name = "Deal"
        indexes = [models.Index(fields=['delas'])]
    
    def __str__(self):
        return self.delas
    
class Slider(models.Model):
    barnd_name=models.ForeignKey(Brand, on_delete=models.CASCADE,blank=True,verbose_name="Brand Name",db_index=True)
    discount=models.IntegerField(blank=True,db_index=True)
    sales=models.CharField(max_length=100)
    discount_deals=models.ForeignKey(Deals, on_delete=models.CASCADE,blank=True,verbose_name="Discount Deals")
    image=models.ImageField(upload_to='media/slimgs/', blank=True,default=True,verbose_name="Slider Image",db_index=True)
    link=models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Slider"
        indexes = [models.Index(fields=['barnd_name','image','discount'])]

    def __str__(self) -> str:
        return self.barnd_name.name
    
class FeaturesArea(models.Model):
    icon=models.CharField(max_length=100)
    title=models.CharField(max_length=100,default="Feature Title",db_index=True)
    description=models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Feature Area"
        indexes = [models.Index(fields=['title'])]
    
    def __str__(self) -> str:
        return self.title
    
class Banner_Top(models.Model):
    deals=models.ForeignKey(Deals, on_delete=models.CASCADE,blank=True,verbose_name="Discount Deals",db_index=True)
    image=models.ImageField(upload_to='media/banner_top_imgs/' ,default=False,)
    discount=models.IntegerField()
    quote=models.CharField(max_length=100)
    link=models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Top Banner"
        indexes = [models.Index(fields=['deals'])]
    
    # def __str__(self) -> str:
    #     return self.deals
    
class Banner_Middle(models.Model):
    deals=models.ForeignKey(Deals, on_delete=models.CASCADE,blank=True,verbose_name="Discount Deals",db_index=True)
    image=models.ImageField(upload_to='media/bamiddle_imgs/',null=True, blank=True)
    quote=models.CharField(max_length=100,db_index=True)
    discount=models.IntegerField()
    link=models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Banner Middle"
        indexes = [models.Index(fields=['deals','quote'])]
    
    def __str__(self) -> str:
        return self.quote
    
class Banner_Button(models.Model):
    title=models.CharField(max_length=100)
    deals=models.ForeignKey(Deals, on_delete=models.CASCADE,blank=True,verbose_name="Discount Deals",db_index=True)
    image=models.ImageField(upload_to='media/bannutton_imgs/',default=False,db_index=True)
    discount=models.IntegerField()
    link=models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Banner Button"
        indexes = [models.Index(fields=['title','deals'])]
    
    def __str__(self):
        
        return self.title
    
class Banner_Bottom_middle(models.Model):
    title=models.CharField(max_length=100,db_index=True)
    deals=models.ForeignKey(Deals, on_delete=models.CASCADE,blank=True,verbose_name="Discount Deals",db_index=True)  
    image=models.ImageField(upload_to='media/bannutton_imgs/',default=False)
    link=models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Banner Bottom Middle"
        indexes = [models.Index(fields=['deals','title'])]
        
    def __str__(self):
        return self.title

    
class Moveing_text(models.Model):
    text1=models.CharField(max_length=100,blank=True,db_index=True)
    text2=models.CharField(max_length=100,blank=True)
    text3=models.CharField(max_length=100,blank=True)
    
    class Meta:
        verbose_name = "Moveing Text"
        indexes = [models.Index(fields=['text1'])]
    
    def __str__(self):
        return self.text1
    
class Top_deals(models.Model):
    name=models.ForeignKey(Product, on_delete=models.CASCADE,db_index=True)
    
    class Meta:
        verbose_name = "Top Deal"
        indexes = [models.Index(fields=['name'])]
    
    def __str__(self):
        return self.name.name
    
class Top_sell(models.Model):
    name=models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name="Product Name",db_index=True)
    
    class Meta:
        verbose_name = "Top Sell"
        indexes = [models.Index(fields=['name'])]
    
    def __str__(self):
        return self.name.name
    
class Special_offer(models.Model):
    name=models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name="Product Name",db_index=True)
    
    class Meta:
        verbose_name = "Special Offer"
        indexes = [models.Index(fields=['name'])]
    
    def __str__(self):
        return self.name.name
    
    
    # footer section start here 
class SocialMediaLink(models.Model):
    name = models.CharField(max_length=100,db_index=True)
    url = models.URLField(db_index=True)
    icon = models.CharField(max_length=100) 
    
    
    class Meta:
        verbose_name = "Social Media Link"
        indexes = [models.Index(fields=['name'])]

    def __str__(self):
        return self.name
    
class CustomerCare(models.Model):
    name=models.CharField(max_length=100,db_index=True)
    link=models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Customer Care"
        indexes = [models.Index(fields=['name'])]
    
    def __str__(self):
        return self.name
    
class CustomerService(models.Model):
    name=models.CharField(max_length=100,db_index=True)
    link=models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Customer Service"
        indexes = [models.Index(fields=['name'])]
    
    def __str__(self):
        return self.name

class Myaccount(models.Model):
    name=models.CharField(max_length=100,db_index=True)
    link=models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "My Account"
        indexes = [models.Index(fields=['name'])]
    
    def __str__(self):
        return self.name


class Quicklinks(models.Model):
    name=models.CharField(max_length=100,db_index=True)
    link=models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Quick Link"
        indexes = [models.Index(fields=['name'])]
    
    def __str__(self):
        return self.name

class Aboutstore(models.Model):
    descr=models.CharField(max_length=100,verbose_name="Discription",db_index=True)
    icon = models.CharField(max_length=100) 
    number=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "About Store"
        indexes = [models.Index(fields=['descr'])]
    
    def __str__(self):
        return self.descr

class Footerlinks(models.Model):
    name=models.CharField(max_length=100,db_index=True)
    link=models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Footer Links"
        indexes = [models.Index(fields=['name'])]
    
    def __str__(self):
        return self.name

class payment_img(models.Model):
    link=models.CharField(max_length=100)
    image=models.ImageField(upload_to='media/payment_img/')
    
    class Meta:
        verbose_name = "Payment Image"
    
    def __str__(self):
        return self.link
    
