from django.db import models

# Create your models here.

class Message(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} - {self.created_at:%d/%m/%Y %H:%M:%S}"