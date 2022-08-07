from itertools import product
from unicodedata import category
from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=20)
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    price = models.IntegerField()
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    imege = models.ImageField(upload_to = "shop/images")

    def __str__(self):
        return self.product_name