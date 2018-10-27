from django.db import models
from django.contrib.auth import settings



# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=150)
    content=models.TextField()
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    images=models.ImageField()

    def __str__(self):
        return self.title