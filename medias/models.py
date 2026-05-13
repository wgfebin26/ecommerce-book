from django.db import models

# Create your models here.
class media(models.Model):
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)


    def __str__(self):
        return 'hi'