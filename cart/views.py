from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from store.models import Product
from .models import Cart
from .models import CartItem

#@login_required
def cart_view(request):
    cart = Cart.objects.get(user=request.user)
    return render(request, 'store/cart/cart.html', {'cart':cart})

def cart_agg(request, product_id, qty):
    #verificar si el usuario esta autenticado
    if request.user.is_authenticated:
        #verificar si el usuario tiene carrito
        if Cart.objects.filter(user=request.user).exists():        
            cart = Cart.objects.get(user=request.user)
            product_1 = Product.objects.get(id=product_id)
            cart.add_to_cart(product_1, qty)
            return HttpResponse("habia carrito, funciono")
        else:
            cart = Cart.objects.create(user = request.user)
            product_2 = Product.objects.get(id=product_id)
            cart.add_to_cart(product_2, qty)
            return HttpResponse("no habia carrito, funciono")
            
    else:
        return render(request, 'customer/error.html')
         