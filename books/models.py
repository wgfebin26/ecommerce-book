from django.db import models

# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=100)


    def __str__(self):
        return self.name
    
class Book(models.Model):
    category=models.ForeignKey(category,on_delete=models.CASCADE,related_name='books')
    bookname=models.CharField(max_length=100)
    Author=models.CharField(max_length=100)
    price=models.IntegerField()
    offerprice=models.IntegerField()
    description=models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)

    def __str__(self):
        return self.bookname