from django.db import models
from .product import Product
from .customer import Customer
# from .OrderItem import OrderItem
import datetime
from django.contrib.auth.models import User

class Order(models.Model):
    # product = models.ForeignKey(Product,
    #                             on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    # quantity = models.IntegerField(default=1)
    # price = models.IntegerField()
    # address = models.CharField(max_length=50, default='', blank=True)
    # phone = models.CharField(max_length=50, default='', blank=True)
    # date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, null=True)

    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total= sum([item.get_total for item in orderitems])
        return total
    @property
    def get_cart_tax(self):
        orderitems = self.orderitem_set.all()
        total= sum([item.get_total for item in orderitems])
        tax = 0.088*total
        return tax
    @property
    def get_cart_final_total(self):
        orderitems = self.orderitem_set.all()
        total= sum([item.get_total for item in orderitems])
        tax = 0.088*total
        return tax+total
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total= sum([item.quantity for item in orderitems])
        return total
    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')
        
    def __str__(self):
        return str(self.id)

#changed

