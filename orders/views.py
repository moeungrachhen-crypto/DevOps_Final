from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from cart.models import Cart
from .models import Order


@login_required
def checkout(request):

    cart = Cart.objects.get(user=request.user)

    if request.method == 'POST':

        order = Order.objects.create(
            user=request.user,
            total_price=cart.total_price
        )

        cart.items.all().delete()

        return redirect('home')

    return render(
        request,
        'orders/checkout.html',
        {
            'cart': cart
        }
    )