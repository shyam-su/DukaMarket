from django.db import models

# Create your models here.
class Banner(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    description = models.TextField(blank=True, null=True, verbose_name="Banner Text")
    image = models.ImageField(upload_to='media/about_banner/', null=True, blank=True)
    button_link = models.CharField(max_length=50, null=True, blank=True)
    
    class Meta:
        verbose_name = "Banner"
        ordering = ['title']
        indexes = [models.Index(fields=['title'])]  # Add index to improve query performance

    def __str__(self):
        return "About Us"

class AboutSection(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    sub_desc = models.TextField(verbose_name="Short Description")
    description = models.TextField()
    image = models.ImageField(upload_to='media/about_section/', null=True, blank=True)
    
    class Meta:
        verbose_name = "About Section"
        ordering = ['title']
        indexes = [models.Index(fields=['title'])]

    def __str__(self):
        return "About Our Online Store"

class Service(models.Model):
    services_area_title = models.CharField(max_length=200, null=True, blank=True, default='services_area_title')
    services_area_description = models.TextField(default='services_area_description')
    title = models.CharField(max_length=100, blank=False, null=False, db_index=True)
    description = models.TextField(blank=False, null=False)
    icon_class = models.CharField(max_length=50, blank=False, null=False)
    step_number = models.PositiveIntegerField(blank=False, null=False)
    
    class Meta:
        verbose_name = "Service"
        ordering = ['step_number']  
        indexes = [models.Index(fields=['title']), models.Index(fields=['step_number'])] 

    def __str__(self):
        return "HOW IT WORKS"

class TechnologyIndex(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    image = models.ImageField(upload_to='media/about_technology/', verbose_name="Image 1")
    images = models.ImageField(upload_to='media/about_technology/', null=True, blank=True, verbose_name="Image 2")
    active_clients = models.PositiveIntegerField(verbose_name="Active Clients In Number")
    projects_done = models.PositiveIntegerField(verbose_name="Projects Done In Number")
    team_advisors = models.PositiveIntegerField(verbose_name="Team Advisors In Number")
    users_online = models.PositiveIntegerField(verbose_name="Users Online In Number")
    
    class Meta:
        verbose_name = "Technology"
        ordering = ['title']
        indexes = [models.Index(fields=['title'])]

    def __str__(self):
        return "Technology Index"

class TeamMember(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    descr = models.CharField(max_length=255, blank=True, null=True, verbose_name="Short Description")
    name = models.CharField(max_length=255, db_index=True)
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/about_team/')
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    dribbble = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Team Member"
        ordering = ['name'] 
        indexes = [models.Index(fields=['name'])]

    def __str__(self):
        return "THE TEAM"
        
class Location(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    descr = models.CharField(max_length=255, blank=True, null=True, verbose_name="Short Description")
    address = models.CharField(max_length=255, db_index=True)
    city = models.CharField(max_length=255, db_index=True)
    country = models.CharField(max_length=255, db_index=True)
    image = models.ImageField(upload_to='media/about_location/')
    map_link = models.URLField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    
    class Meta:
        verbose_name = "Location"
        ordering = ['city', 'address']  # Ordered by city and address for logical sorting
        indexes = [models.Index(fields=['city', 'address'])]  # Composite index for address and city

    def __str__(self):
        return f'{self.address}, {self.city}'


