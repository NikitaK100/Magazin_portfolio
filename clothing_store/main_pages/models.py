from itertools import product
from turtle import mode
from django.db import models
from django.forms import BooleanField
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории'


class SubCategory(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Под-категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("sub_category", kwargs={"cat_slug": self.category.slug, "cat_sub_slug": self.slug})

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name_plural = 'Под-категории'


class Products(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Название товара')
    description = models.TextField(max_length=700, blank=False, verbose_name='Описание товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    structure = models.CharField(max_length=100, verbose_name='Состав')
    color = models.CharField(max_length=100, verbose_name='Цвет')
    discount = models.IntegerField(default=0, verbose_name='Скидка(в процентах)')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    sub_cat = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='Подкатегория')
    quantity = models.IntegerField(default=0, verbose_name='Кол-во товара')


    def get_absolute_url(self):
        return reverse("sub_category", kwargs={"cat_slug": self.sub_cat.category.slug, "cat_sub_slug": self.sub_cat.slug, 
        'product_slug': self.slug})

    def __str__(self):
        return str(self.name)

    def get_discount(self):
        price = int(self.price * (100 - self.discount) / 100)
        return price 


    class Meta:
        verbose_name_plural = 'Товары'


class Images(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d')
    is_main = models.BooleanField(default=False, verbose_name='Главная?')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return str(self.product.name)


class Sizes(models.Model):
    size = models.CharField(max_length=10, verbose_name='Размеры')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='sizes')

    def __str__(self):
        return str(self.product.name)









    
