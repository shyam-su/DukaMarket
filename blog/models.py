from django.db import models
from datetime  import datetime
from shop.models import Category
from django.utils.text import slugify


# Create your models here.
class Blog_Banner(models.Model):
    title = models.CharField(max_length=255,blank=True, null=True,db_index=True)
    image = models.ImageField(upload_to='media/blog_banner/',null=True, blank=True)
    
    class Meta:
        verbose_name = "Blog Banner"
        ordering = ['title']
        indexes = [models.Index(fields=['title'])] 


    def __str__(self):
        return "Blog Banner"

class Tag(models.Model):
    name=models.CharField(max_length=100,db_index=True)
    link=models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Blog Tag"
        indexes = [models.Index(fields=['name'])]

    
    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title=models.CharField(max_length=100,db_index=True)
    author=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image')
    content=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE,db_index=True)
    slug=models.SlugField(max_length=100, unique=True,null=True,default=None)
    date=models.DateField(auto_now_add=True)
    tag=models.ForeignKey(Tag, on_delete=models.CASCADE,null=True, blank=True)
    status = models.CharField(max_length=10, choices=[('draft', 'Draft'), ('published', 'Published')],db_index=True)
    
    class Meta:
        verbose_name = "Blog"
        indexes = [models.Index(fields=['title','category','status'],)]
    
    def save(self, *args, **kwargs):
            if not self.slug:  # Use the correct field name
                self.slug = slugify(self.title)
            super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.title} ({self.category})"
    
class Comment(models.Model):
    id=models.AutoField(primary_key=True)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE,related_name='comments',db_index=True)
    name = models.CharField(max_length=80,db_index=True)
    email=models.EmailField()
    website = models.URLField(blank=True,null=True)
    comment = models.TextField()
    date=models.DateTimeField(default=datetime.now)
    
    class Meta:
        verbose_name = "Comments"
        indexes = [models.Index(fields=['name','post'])]
         
    def __str__(self):
        return self.name
    
class Reply(models.Model):
    id=models.AutoField(primary_key=True)
    post = models.ForeignKey(Comment, on_delete=models.CASCADE,related_name='reply')
    name = models.CharField(max_length=80)
    email=models.EmailField()
    website = models.URLField(blank=True,null=True)
    comment = models.TextField()
    date=models.DateTimeField(default=datetime.now)
    
    class Meta:
        verbose_name = "Reply"
         
    def __str__(self):
        return self.name
    
    

class Blog_Details_Banner(models.Model):
    title = models.CharField(max_length=255,blank=True, null=True)
    image = models.ImageField(upload_to='media/blog_deatils_banner/',null=True, blank=True)
    
    class Meta:
        verbose_name = "Blog Details Banner"
        ordering = ['title']

    def __str__(self):
        return "Blog Details Banner"
