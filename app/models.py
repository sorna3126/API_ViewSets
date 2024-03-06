from django.db import models

# Create your models here.

class Product_Category(models.Model):
    Product_Category_id=models.IntegerField(primary_key=True)
    Product_Category_name=models.CharField(max_length=100)

    def __str__(self):
        return self.Product_Category_name

class Product(models.Model):
    Product_Category_id=models.ForeignKey(Product_Category,on_delete=models.CASCADE)
    Product_id=models.IntegerField()
    Product_name=models.CharField(max_length=100)
    Product_Price=models.IntegerField()
    Product_brand=models.CharField(max_length=100)







