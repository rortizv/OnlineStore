from django.contrib import admin

from ordersManagement.models import Clients, Products, Orders

class AdminClients(admin.ModelAdmin):
    list_display = ('full_name', 'address', 'phone')
    search_fields = ('full_name', 'address', 'phone')

class AdminProducts(admin.ModelAdmin):
    list_filter = ('category',)
    list_display = ('name', 'category', 'price')
    search_fields = ('name', 'category', 'price')

class AdminOrders(admin.ModelAdmin):
    list_display = ('number', 'date')
    list_filter = ('delivered',)
    date_hierarchy = 'date'

admin.site.register(Clients, AdminClients)
admin.site.register(Products, AdminProducts)
admin.site.register(Orders)