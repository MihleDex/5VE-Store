from pyexpat import model
from django.db import models
from sqlalchemy import null
from django.contrib.auth.models import User

# Create your models here.
class Items(models.Model):
    item_name = models.CharField(max_length=20)
    item_price = models.CharField(max_length=20)
    item_image = models.ImageField(null=True ,blank = True,upload_to= "static/img/")
    item_page = models.CharField(max_length=200)
    on_stock = models.BooleanField()

    def __str__(self):
        return self.item_name

    
class NewsLetter(models.Model):
    email = models.EmailField(max_length=200)


class UserItem(models.Model):
    product = models.ForeignKey(Items, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return self.quantity * float(self.product.item_price)

    def __str__(self):
        return self.product.item_name

class UserOrder(models.Model):
    order_number = models.CharField(max_length=50)
    items = models.ManyToManyField(UserItem)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

