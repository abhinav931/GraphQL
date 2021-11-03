from django.db import models
# Create your models here.


class Flavor(models.Model):
    name = models.CharField(
        null=False, blank=False, max_length=200)


class Cake(models.Model):
    name = models.CharField(
        null=False, blank=False, max_length=200)
    is_decorated = models.BooleanField(default=False)
    price = models.FloatField(default=5.0)
    flavor = models.ForeignKey(Flavor, on_delete=models.PROTECT)
