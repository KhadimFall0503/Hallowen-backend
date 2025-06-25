from django.db import models

# Create your models here.
class Candies(models.Model):
    image = models.ImageField(upload_to='uploads/candies/')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    def __str__(self):
        return self.name


class Decorations(models.Model):
    image = models.ImageField(upload_to='uploads/decorations/')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name
