from django.shortcuts import render
from django.http import HttpResponse
from ordersManagement.models import Products
from django.core.mail import send_mail
from django.conf import settings
from ordersManagement.forms import ContactForm


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
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            send_mail(data['subject'], data['message'], data.get('email', ''), ['rafael289@hotmail.com'],)
            return HttpResponse(request, 'thanks.html')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})