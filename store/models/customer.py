from django.db import models

class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=50)

    @staticmethod
    def get_customer_by_id(email):
        return Customer.objects.filter(email=email)
    
    @staticmethod
    def get_by_id(id):
        return Customer.objects.filter(id=id)
    
    def showpass(self):
        print(self.password)