from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product  , cart):
    pass
    # keys = cart.keys()
    # for id in keys:
    #     if int(id) == product.id:
    #         return True
    # return False;


@register.filter(name='cart_quantity')
def cart_quantity(product  , cart):
    pass
    # keys = cart.keys()
    # for id in keys:
    #     if int(id) == product.id:
    #         return cart.get(id)
    # return 0;


@register.filter(name='price_total')
def price_total(product  , cart):
    pass
    # return product.price * cart_quantity(product , cart)


@register.filter(name='total_cart_price')
def total_cart_price(products , cart):
    pass
    # sum = 0 ;
    # for p in products:
    #     sum += price_total(p , cart)

    # return sum
    