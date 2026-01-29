from django.db import models

# Create your models here.
class Note(models.Model):
    content = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)