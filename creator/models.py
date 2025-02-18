
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Creator(models.Model):
    title = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/creators')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username