from photo.models import Photo
from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
	list_display = ['id', 'author', 'text', 'image', 'created', 'updated']
	list_display_links = ['id', 'author', 'text', 'image', 'created', 'updated']
