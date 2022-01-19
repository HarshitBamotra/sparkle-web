from django.db import models
from .product import Product
from .order import Order
from .customer import Customer


class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null = True, blank= True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null = True, blank= True)
    receiver_name = models.CharField(max_length=250, null= True)
    address_line_1 = models.CharField(max_length=250, null=True)
    address_line_2 = models.CharField(max_length=250, null=True)
    city = models.CharField(max_length=250, null=True)
    state = models.CharField(max_length=250, null=True)
    zip = models.CharField(max_length=250, null=True)
    receiver_phone = models.CharField(max_length=15)
    receiver_email = models.EmailField()
    express_shipping = models.BooleanField(default=False)

    def __str__(self):
        return str(self.order)
    @property
    def shipping_total(self):
        total_payable = self.order.get_cart_final_total
        if self.express_shipping == True:
            total_payable+=20
        return total_payable
            
    
    