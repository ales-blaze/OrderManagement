from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    image = models.URLField(max_length=500)
    description = models.TextField(blank=True , null=True)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# class Offers(models.Model):
#     code = models.CharField(max_length=8)
#     discount = models.SmallIntegerField()
#
#     def __str__(self):
#         return self.code
