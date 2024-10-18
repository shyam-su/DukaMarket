from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth import get_user_model



# Create your models here.
User = get_user_model()

class ShopBanner(models.Model):
    text=models.CharField(max_length=100,null=True, blank=False,db_index=True)
    button=models.CharField(max_length=100,null=True, blank=False)
    image=models.ImageField(upload_to='shop_banners/',null=True, blank=False)
    
    class Meta:
        verbose_name = "Shop Banner"
        indexes = [models.Index(fields=['text'])]
    
    def __str__(self):
        return self.text

class Category(models.Model):
    name = models.CharField(max_length=255,null=True, blank=False ,verbose_name="Category Name",db_index=True)
    
    class Meta:
        verbose_name = "Category"
        indexes = [models.Index(fields=['name'])]   

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name=models.CharField(max_length=255,null=True, blank=False,verbose_name="Brand Name",db_index=True)
    image=models.ImageField(upload_to='media/brand_imgs/', blank=True,default=True)
    
    class Meta:
        indexes = [models.Index(fields=['name'])]

    
    def __str__(self):
        return self.name
    

class Size(models.Model):
    name = models.CharField(max_length=255,null=True, blank=False,verbose_name="Size Name",db_index=True)
    
    class Meta:
        indexes = [models.Index(fields=['name'])]


    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=255,verbose_name="Tag Name",null=True, blank=True,db_index=True)
    
    class Meta:
        indexes = [models.Index(fields=['name'])]

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255,null=False, blank=False,verbose_name="Product Name",db_index=True)
    description = CKEditor5Field(null=True, blank=True,db_index=True)
    additional_information = CKEditor5Field(null=True, blank=True,config_name='extends',db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=False, blank=False,verbose_name="Product Price",db_index=True)
    discount=models.DecimalField(decimal_places=3, max_digits=5,null=True, blank=True,db_index=True)
    availability = models.IntegerField(null=True, blank=True,db_index=True)
    sku = models.CharField(max_length=100,null=True, blank=True,db_index=True)
    size=models.ForeignKey(Size, on_delete=models.CASCADE,null=True, blank=True,db_index=True)
    image = models.ImageField(upload_to='products/',null=True, blank=True,db_index=True)
    features = CKEditor5Field(null=True, blank=True,db_index=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE,null=True, blank=True,db_index=True)
    tags=models.ForeignKey(Tag, on_delete=models.CASCADE,null=True, blank=True,db_index=True)
    stock=models.IntegerField(null=True, blank=True,db_index=True)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, null=True, blank=True,db_index=True)
    
    class Meta:
        verbose_name = "Product"
        indexes = [models.Index(fields=['name','description','additional_information','price','discount','availability','sku','size','image','features','categories','tags','stock','brand'])]


    def __str__(self):
        return self.name

class Reviews(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE,db_index=True)
    review=models.IntegerField(default=0,null=True, blank=False)
    name=models.CharField(max_length=100,db_index=True)
    email=models.EmailField()
    comment=models.TextField(max_length=100)
    
    class Meta:
        verbose_name = "Product Review"
        indexes = [models.Index(fields=['product','name'])]

    
    def __str__(self):
        return self.product.name
    
    
class Cart_banner(models.Model):
    title=models.CharField(max_length=255,null=True, blank=False,db_index=True)
    Bg_image=models.ImageField(upload_to='media/cart_imgs/', blank=True, null=True)
    
    class Meta:
        verbose_name = "Cart Banner"
        indexes = [models.Index(fields=['title'])]

    
    def __str__(self):
        return self.title
    
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,db_index=True)
    quantity = models.PositiveIntegerField(default=0)
    unitprice=models.PositiveIntegerField(default=0)
    total=models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE,db_index=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Cart Item"
        indexes = [models.Index(fields=['product','user'])]
    
    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
    
    
    def save(self, *args, **kwargs):
        self.unitprice = self.product.price
        self.total = self.quantity * self.unitprice
        super().save(*args, **kwargs)


class Checkout_banner(models.Model):
    title=models.CharField(max_length=255,null=True, blank=False,db_index=True)
    image=models.ImageField(upload_to='media/cart_imgs/', blank=True, null=True)
    
    class Meta:
        verbose_name = "Checkout Banner"
        indexes = [models.Index(fields=['title'])]
    
    def __str__(self):
        return self.title
    
class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,db_index=True)
    first_name = models.CharField(max_length=100,db_index=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(db_index=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    phone=models.CharField(max_length=20,db_index=True)
    
    class Meta:
        verbose_name = "Checkout"
        indexes = [models.Index(fields=['user','first_name','email','phone'])]


    def __str__(self):
        return f"Order {self.id} by {self.user}"

class Order(models.Model):
    Payment_Method = {
        ('Cash on Delevery', 'Cash on Delevery'),
        ('Khalti', 'Khalti'),
        
    }
    product = models.CharField(max_length=255,db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    total_price=models.DecimalField(max_digits=10, decimal_places=2)
    payment_method=models.CharField(max_length=255,db_index=True)
    status=models.CharField(max_length=255,db_index=True)
    
    class Meta:
        verbose_name = "All Order"
        indexes = [models.Index(fields=['product','payment_method','status'])]

    def __str__(self):
        return f"{self.quantity} x {self.product}"