
# Create your views here.
from django.shortcuts import render
from django.contrib.auth import get_user_model

from products.models import Product, Category
from orders.models import Order

User = get_user_model()


def dashboard(request):

    total_products = Product.objects.count()

    total_categories = Category.objects.count()

    total_orders = Order.objects.count()

    total_users = User.objects.count()

    total_revenue = sum(
        order.total_price
        for order in Order.objects.all()
    )

    context = {
        'total_products': total_products,
        'total_categories': total_categories,
        'total_orders': total_orders,
        'total_users': total_users,
        'total_revenue': total_revenue,
    }

    return render(
        request,
        'dashboard/dashboard.html',
        context
    )