from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=100)
    
    #overriding the function so it now displays category name rather than object name
    def __str__(self):
        return self.name
    
    @staticmethod
    def get_all_categories():
        return Category.objects.all()