from django.db import models


# Here builiding models to store information

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=200)

    def __str__(self):
        return self.name
    

class Shop(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=200)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name


class SupplyDetails(models.Model):
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)   
    quantity = models.IntegerField() 