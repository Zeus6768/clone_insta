from django.contrib.auth.models import User, update_last_login
from django.db import models
from django.urls import reverse

# Create your models here.

class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='timeline_photo/%Y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        if len(self.text) < 20:
            return self.text
        else:
            return self.text[:20] + "..."

    def get_absolute_url(self):
        return reverse('photo:detail', args=[self.id])