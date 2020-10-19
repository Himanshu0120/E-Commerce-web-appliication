from django.db import models
from .category import Category


class Product(models.Model):
    
    name=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    description=models.CharField(max_length=200,null=False)
    image=models.ImageField(upload_to='uploads/products/')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)

    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    @staticmethod
    def get_products_byId(category_r):
        if category_r:
            return Product.objects.filter(category=category_r)
        else:
            return Product.objects.all()
    
    @staticmethod
    def get_by_id(ids):
        return Product.objects.filter(id__in=ids)