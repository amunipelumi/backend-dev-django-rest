from django.db import models
from django.db.models import Q
from django.conf import settings
import random


User = settings.AUTH_USER_MODEL
ALGO_TAGS = ['cars', 'bikes', 'motor']

class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)
    
    def search(self, query, user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.is_public().filter(lookup)

        if user:
            qs1 = self.filter(user=user).filter(lookup)
            qs = (qs | qs1).distinct()

        return qs


class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(model=self.model, using=self._db)
    
    def search(self, query, user=None):
        # return Product.objects.filter(public=True).filter(title__icontains=query)
        return self.get_queryset().search(query, user=user)


class Product(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=125)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    public = models.BooleanField(default=True)
    objects = ProductManager()

    def is_public(self):
        return self.public
    
    def get_tags(self):
        return [random.choice(ALGO_TAGS)]

    @property
    def sale_price(self):
        return '%.2f' %(float(self.price) * 0.8)
    
    def discount(self):
        return '20%'