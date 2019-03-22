from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    image = models.ImageField()
    description = models.TextField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Offers(models.Model):
    code = models.CharField(max_length=8)
    discount = models.SmallIntegerField()

    def __str__(self):
        return self.code
