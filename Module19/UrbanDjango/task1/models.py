from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(decimal_places=2, max_digits=9)
    age = models.IntegerField()

    def __lt__(self, other):
        return self < other


class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(decimal_places=2, max_digits=8)
    size = models.DecimalField(decimal_places=1, max_digits=4)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')
