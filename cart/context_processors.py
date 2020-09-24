from .cart import Cart


# instantiate the car with the request object and make it
# available for the templates as the variable: cart

def cart(request):
    return {'cart': Cart(request)}
