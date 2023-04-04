from django.shortcuts import render
from django.http import HttpResponse
from ordersManagement.models import Products


def search_products(request):
    return render(request, 'search_products.html')

def search(request):
    if request.GET['product']:
        # message = "Product searched: %r" %request.GET['search']
        product = request.GET['product']
        if len(product)>20:
            message = "Text is too long."
        else:
            products = Products.objects.filter(name__icontains=product)
            return render(request, 'search_results.html', {'products': products, 'query': product})
    else:
        message = "You submitted an empty form."
    return HttpResponse(message)

def contact(request):
    if request.method == 'POST':
        return render(request, 'thanks.html')
    return render(request, 'contact.html')