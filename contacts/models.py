from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phonenum=models.IntegerField()
    description=models.CharField(max_length=200)

    def __str__(self):
        return self.name