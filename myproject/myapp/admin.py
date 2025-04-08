from django.contrib import admin
from .models import Image

admin.site.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'photo', 'date']
