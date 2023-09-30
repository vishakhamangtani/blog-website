from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(models.Model):
    # Auto-generated user ID
    # Primary Key 'id' is automatically created by Django
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)  # Assuming a simple string for phone number
    # categories = models.ManyToManyField(Category, blank=True)
    password = models.CharField(max_length=255)  # Store hashed passwords for security
    
class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog_images/') 
    date_published = models.DateTimeField(auto_now_add=True)
    content = models.TextField()