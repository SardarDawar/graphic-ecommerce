from django.shortcuts import render, get_object_or_404
from .models import Product
from bag.forms import CartAddProductForm


def all_products(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    cart_product_form = CartAddProductForm()

    context = {
        'product': product,
        'cart_product_form':cart_product_form,
    }

    return render(request, 'products/product_detail.html', context)



