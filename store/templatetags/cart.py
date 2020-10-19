from django import template

register=template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    if str(product) in cart.keys():
        return True
    else:
        return False

@register.filter(name='cart_count')
def cart_count(product,cart):
    return cart[str(product)]

@register.filter(name='item_total')
def item_total(product,cart):
    return (int(cart[str(product.id)])*product.price)

@register.filter(name='total')
def total(products,cart):
    sum=0
    for product in products:
        sum+=product.price*(int(cart[str(product.id)]))
    return sum