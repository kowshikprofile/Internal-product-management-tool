from django.shortcuts import render, get_object_or_404
from .models import Product, ProductAttributeValue

# Show all products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'catalog/product_list.html', {'products': products})

# Show details of a single product
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    attributes = ProductAttributeValue.objects.filter(product=product)
    return render(request, 'catalog/product_detail.html', {
        'product': product,
        'attributes': attributes
    })