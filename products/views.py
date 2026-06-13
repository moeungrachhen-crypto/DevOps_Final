from django.shortcuts import render, get_object_or_404
from .models import Product
from django.contrib.auth.decorators import login_required
from .models import Product, Category

def home(request):
    products = Product.objects.all()[:8]
    categories = Category.objects.all()

    return render(
        request,
        'products/home.html',
        {
            'products': products,
            'categories': categories,
        }
    )


def product_list(request):
    products = Product.objects.all()

    return render(
        request,
        'products/product_list.html',
        {'products': products}
    )


def product_detail(request, pk):
    product = get_object_or_404(
        Product,
        id=pk
    )

    return render(
        request,
        'products/product_detail.html',
        {'product': product}
    )

    from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Product


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def product_list(request):
    products = Product.objects.all()

    return render(
        request,
        'products/product_list.html',
        {'products': products}
    )


@login_required
def product_detail(request, pk):
    product = Product.objects.get(pk=pk)

    return render(
        request,
        'products/product_detail.html',
        {'product': product}
    )



@login_required
def home(request):
    return render(
        request,
        'products/home.html'
    )

    from .models import Product, Category

def home(request):

    products = Product.objects.all()[:8]
    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories,
    }

    return render(
        request,
        'products/home.html',
        context
    )
def category_products(request, category_id):

    category = get_object_or_404(
        Category,
        id=category_id
    )

    products = Product.objects.filter(
        category=category
    )

    return render(
        request,
        'products/category_products.html',
        {
            'category': category,
            'products': products
        }
    )