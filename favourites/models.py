from django.db import models
from products.models import Product
from django.contrib.auth.models import User


class Favourites(models.Model):
    # id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.user

    class Meta:
        ordering = ['-id']
