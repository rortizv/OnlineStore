from django.db import models


class Clients(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name

class Products(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return 'Product %s in category %s with price %s' % (self.name, self.category, self.price)

class Orders(models.Model):
    number = models.IntegerField()
    date = models.DateField()
    delivered = models.BooleanField()