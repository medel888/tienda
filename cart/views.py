from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def cart(request):
    return render(request, 'store/cart/cart.html')
