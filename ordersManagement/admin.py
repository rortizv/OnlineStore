from django.contrib import admin

from ordersManagement.models import Clients, Products, Orders

class AdminClients(admin.ModelAdmin):
    list_display = ('full_name', 'address', 'phone')
    search_fields = ('full_name', 'address', 'phone')

admin.site.register(Clients, AdminClients)
admin.site.register(Products)
admin.site.register(Orders)