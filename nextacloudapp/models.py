from django.db import models

# Create your models here.

class Brands(models.Model):
    brand_name = models.CharField(max_length=200 , null=True, blank=True)
    type_of_brand = models.CharField(max_length=200 , null=True, blank=True)

class Store(models.Model):
    store_address = models.CharField(max_length=200 , null=True, blank=True)
    store_name = models.CharField(max_length=200 , null=True, blank=True)
    manager = models.CharField(max_length=200 , null=True, blank=True)
    manager_id = models.CharField(max_length=200 , null=True, blank=True)
    
class EquipmentAndItems(models.Model):
    item = models.CharField(max_length=200 , null=True, blank=True)
    type_item = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    # quantity_in_item = models.IntegerField(null=True , blank=True)
    dollar_value = models.IntegerField(null=True, blank=True)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE, null=True, blank = True)
    condition = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank = True)
    identification_code = models.CharField(max_length=200 , null=True, blank=True)
    size = models.CharField(max_length=200 , null=True, blank=True)
    country_of_origin = models.CharField(max_length=200 , null=True, blank=True)
    