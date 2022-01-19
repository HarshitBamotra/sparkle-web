from django.contrib import admin

from store.models.orderitems import OrderItem
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.order import Order
from .models.cart import ShippingAddress

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']



class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category , AdminCategory)
admin.site.register(Customer )
admin.site.register(Order )
admin.site.register(ShippingAddress)
# admin.site.register(CartItem )
admin.site.register(OrderItem)
