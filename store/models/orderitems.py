from django.db import models
from .product import Product
from .order import Order
from .customer import Customer
import datetime
from django.contrib.auth.models import User

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    data_added= models.DateTimeField(auto_now_add=True)
	
    @property
    def get_total(self):
        total= self.product.price * self.quantity
        return total

    def __str__(self):
        return str(self.order)