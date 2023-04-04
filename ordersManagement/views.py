from django.shortcuts import render
from django.http import HttpResponse
from ordersManagement.models import Products
from django.core.mail import send_mail
from django.conf import settings


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
        subject = request.POST['subject']
        message = request.POST['message']
        email = request.POST['email']
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['rortiz@inkremental.co']
        send_mail(subject, message, email_from, recipient_list)
        return render(request, 'thanks.html')
    return render(request, 'contact.html')