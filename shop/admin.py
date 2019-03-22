from django.contrib import admin
from .models import Products , Offers


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'image']


class OffersAdmin(admin.ModelAdmin):
    list_display = ['code', 'discount']


admin.site.register(Offers, OffersAdmin)
admin.site.register(Products, ProductAdmin)
