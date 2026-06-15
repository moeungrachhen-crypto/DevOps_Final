from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.core.paginator import Paginator
from .models import Product
from .models import Category
from .forms import ProductForm


# =========================
# Home Page
# =========================

def home(request):

    products = Product.objects.all()[:8]

    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories
    }

    return render(
        request,
        'products/home.html',
        context
    )


# =========================
# Product List
# =========================
def product_list(request):

    query = request.GET.get('q')

    products = Product.objects.all().order_by('-id')

    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query)
        )

    paginator = Paginator(products, 8)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': query,
    }

    return render(
        request,
        'products/product_list.html',
        context
    )


# =========================
# Product Detail
# =========================

def product_detail(request, id):

    product = get_object_or_404(
        Product,
        id=id
    )

    context = {
        'product': product
    }

    return render(
        request,
        'products/product_detail.html',
        context
    )


# =========================
# Category Products
# =========================

def category_products(request, category_id):

    category = get_object_or_404(
        Category,
        id=category_id
    )

    products = Product.objects.filter(
        category=category
    )

    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'selected_category': category
    }

    return render(
        request,
        'products/home.html',
        context
    )


# =========================
# Create Product
# =========================

def product_create(request):

    if request.method == 'POST':

        form = ProductForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return redirect(
                'product_list'
            )

    else:

        form = ProductForm()

    context = {
        'form': form
    }

    return render(
        request,
        'products/product_form.html',
        context
    )


# =========================
# Update Product
# =========================

def product_update(request, id):

    product = get_object_or_404(
        Product,
        id=id
    )

    if request.method == 'POST':

        form = ProductForm(
            request.POST,
            request.FILES,
            instance=product
        )

        if form.is_valid():

            form.save()

            return redirect(
                'product_list'
            )

    else:

        form = ProductForm(
            instance=product
        )

    context = {
        'form': form,
        'product': product
    }

    return render(
        request,
        'products/product_form.html',
        context
    )


# =========================
# Delete Product
# =========================

def product_delete(request, id):

    product = get_object_or_404(
        Product,
        id=id
    )

    if request.method == 'POST':

        product.delete()

        return redirect(
            'product_list'
        )

    context = {
        'product': product
    }

    return render(
        request,
        'products/product_confirm_delete.html',
        context
    )