from django.contrib import admin
from .models import Car, brand

class CarAdmin(admin.ModelAdmin):
    list_display = ('Id', 'model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand',)

admin.site.register(Car, CarAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display = ( 'name',)
    search_fields = ('name',)   

admin.site.register(brand, BrandAdmin)