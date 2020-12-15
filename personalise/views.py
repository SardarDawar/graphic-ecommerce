from django.shortcuts import render, get_object_or_404
from products.models import Product


def personalise(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'personalise.html', context)
