from django.shortcuts import render , redirect
from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import  Product

class Favorite(View):
    def get(self , request):
        ids = list(request.session.get('favorite').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request , 'favorite.html' , {'products' : products} )
