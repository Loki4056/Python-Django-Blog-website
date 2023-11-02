from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields to store user profile information
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='static/profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class Article(models.Model):    
    title = models.CharField(max_length=255)
    content = HTMLField()
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    image = models.ImageField(upload_to='article_images/', blank=False, null=False)

    def __str__(self):
        return self.title
