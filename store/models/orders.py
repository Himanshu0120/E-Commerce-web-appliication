from django.db import models
from .product import Product
import datetime
from .customer import Customer
class Orders(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    date=models.DateField(default=datetime.datetime.today)
    phone=models.CharField(max_length=15,default='')
    address=models.CharField(max_length=200,default='')
    status=models.BooleanField(default=False)

    def place_order(self):
        self.save()
    
    @staticmethod
    def get_order_by_customer(customer):
        return Orders.objects.filter(customer=customer)