from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, help_text="Enter a descriptive name for the image")
    description = models.TextField(blank=True, null=True, help_text="Enter a description for the image")
    photo = models.ImageField(upload_to="myimage")
    date = models.DateTimeField(auto_now_add=True)
