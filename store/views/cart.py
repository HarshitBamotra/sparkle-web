
from django.shortcuts import render , redirect
from django.contrib.auth.hashers import  check_password
from store.models.cart import CartItem, ShippingAddress
from store.models.customer import Customer
from store.models.order import Order
from store.models.orderitems import OrderItem
from django.views import  View
from store.models.product import  Product
from store.models import *
from django.http import JsonResponse
import json
import datetime
from store.utils import cookieCart, cartData, guestOrder

# class Cart(View):
#     pass
#     def get(self , request):
#         pass
        # ids = list(request.session.get('cart').keys())
        # products = Product.get_products_by_id(ids)
        
        # print(products)
        # total=0
        # for product in products:  
        #     # for id in ids:
        #     #     if int(id) == product.id:
        #     #         print(product.id)
        #     total += product.price
        # print (total)
        # context = {
        #     'products': products,
        #     'total':total,
        # }
        # return render(request , 'cart.html' , context )

def delete_p(request,pid):
    # cart = Product.objects.get(id=pid)
    # cart.delete()
    return redirect('home')

def cart(request):
    if request.user.is_authenticated:
        customer= request.user.customer
        order, created= Order.objects.get_or_create(customer=customer, status= False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookiedata= cookieCart(request)
        items= cookiedata['items']
        order= cookiedata['order']
        cartItems= cookiedata['cartItems']
        

    context= {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'cart.html', context)
# def cart(request):

# 	if request.user.is_authenticated:
# 		customer = request.user.customer
# 		order, created = Order.objects.get_or_create(customer=customer, status=False)
# 		items = order.orderitem_set.all()
#     if not(request.user.is_authenticated):
#         items=[]
#         order={'i':0, 'o':0}

	
# 	context = {'items':items, 'order':order }
# 	return render(request, 'cart.html', context)

def updateItem(request):
        data = json.loads(request.body)
        productId = data['productId']
        action = data['action']
        print('Action:', action)
        print('Product:', productId)

        customer = request.user.customer
        product = Product.objects.get(id=productId)
        order, created = Order.objects.get_or_create(customer=customer, status=False)
        orderitem, created = OrderItem.objects.get_or_create(order=order, product=product)
        if action == 'add':
            orderitem.quantity+=1
        elif action == 'remove':
            orderitem.quantity-=1
        elif action == 'delete':
            orderitem.quantity = 0
            
        
        
        
        if orderitem.quantity <= 0:
            orderitem.delete()

        orderitem.save()
        # orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        
        # if action == 'add':
        # 	orderItem.quantity = (orderItem.quantity + 1)
        # elif action == 'remove':
        # 	orderItem.quantity = (orderItem.quantity - 1)

        # orderItem.save()

        # if orderItem.quantity <= 0:
        # 	orderItem.delete()
        return JsonResponse('Item was added', safe=False)



def checkout(request):
    # data=json.loads(request.body)
    #orderId=data['productId']
    # action = data['action']
    
    data= cartData(request)
    items= data['items']
    order= data['order']
    cartItems= data['cartItems']
    # amount = order.get_cart_final_total
    #shipping.express_shipping = True
    # if shipping.express_shipping == True:
    #     amount+=20
    # if action == 'express':
    #     amount+=20
    context = {'items':items, 'order':order,'cartItems':cartItems}
    return render(request, 'checkout.html', context)
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created= Order.objects.get_or_create(customer=customer, complete=False)
        

        
    else:
        customer, order= guestOrder(request, data)

    total= float(data['form']['total'])
    order.transaction_id = transaction_id
    if total == order.get_cart_total:
        order.status = True
    order.save()

    ShippingAddress.objects.create(
        customer= customer,
        order = order,
        receiver_name= data['shipping']['name'],
        receiver_phone= data['shipping']['phone'],
        receiver_email= data['form']['email'],
        address_line_1= data['shipping']['add1'],
        address_line_2= data['shipping']['add2'],
        city= data['shipping']['city'],
        state= data['shipping']['state'],
        zip= data['shipping']['zip']
    )



    return JsonResponse('Payment Complete', safe=False)

# def update_shipping(request):
#     order, created= Order.objects.get_or_create(customer=customer, status= False)
#     amount = order.get_cart_final_total
#     data = json.loads(request.body)
#     action = data['action']
#     if action=='express':
#         amount+=20
#     context = {'amount':amount}
#     return render(request, 'checkout.html', context)


