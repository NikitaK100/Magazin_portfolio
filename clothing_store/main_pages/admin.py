from django.contrib import admin
from .models import *


class ImagesInline(admin.TabularInline):
    fk_name = 'product'
    model = Images 


class SizesInline(admin.TabularInline):
    model = Sizes
    

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class ProductsAdmin(admin.ModelAdmin):
    inlines = [ImagesInline, SizesInline]
    prepopulated_fields = {'slug': ('name',)}
    

admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Products, ProductsAdmin)

