from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser


class CustomUserManager(BaseUserManager):
    """Custom user manager."""
    
    def create_user(self, email, password=None, **extra_kwargs):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(email=self.normalize_email(email), **extra_kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_kwargs):
        """Create and save a superuser with the given email and password."""
        extra_kwargs.setdefault('is_staff', True)
        extra_kwargs.setdefault('is_superuser', True)
        extra_kwargs.setdefault('is_active', True)

        if extra_kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_kwargs)


class CustomUser(AbstractUser):
    username = None
    full_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50)
    gender = models.CharField(max_length=255, choices=[('Male', 'Male'), ('Female', 'Female')])
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_user_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.'
    )

    REQUIRED_FIELDS = ["full_name"]
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
        indexes = [models.Index(fields=['full_name', 'email', 'phone_number'])]

    def save(self, *args, **kwargs):
        if not self.phone_number.startswith('+977'):
            self.phone_number = '+977' + self.phone_number
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email
