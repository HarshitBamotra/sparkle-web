from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product  , favorite):
    keys = favorite.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False;


@register.filter(name='cart_quantity')
def cart_quantity(product  , favorite):
    keys = favorite.keys()
    for id in keys:
        if int(id) == product.id:
            return favorite.get(id)
    return 0;


@register.filter(name='price_total')
def price_total(product  , favorite):
    return product.price * cart_quantity(product , favorite)


@register.filter(name='total_cart_price')
def total_cart_price(products , favorite):
    sum = 0 ;
    for p in products:
        sum += price_total(p , favorite)

    return sum
    