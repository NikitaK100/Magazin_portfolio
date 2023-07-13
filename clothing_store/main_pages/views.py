from ast import Sub
from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from main_pages.models import Products, Category, SubCategory, Images

from main_pages.utils import DataMixin

# Create your views here.




class MainPageCategory(ListView):

    model = SubCategory
    template_name = 'main_pages/base.html'
    context_object_name = 'subcategories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MainPageCategory, self).get_context_data(**kwargs)
        
        context['categories'] = Category.objects.order_by('-name')
        context['products'] = Products.objects.order_by('-name')[:4]
        context['images'] = Images.objects.filter(is_main=True)
        return context

    def get_queryset(self):
        return SubCategory.objects.all().select_related('category')


class Catalog(ListView):

    model = SubCategory
    template_name = 'main_pages/catalog.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Catalog, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.order_by('-name')
        context['subcategories'] = SubCategory.objects.all()
        return context


class CategoryPages(DetailView):
    model = Category
    slug_url_kwarg = 'cat_slug'
    template_name = 'main_pages/category.html'
    # context_object_name = 'subcategories'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryPages, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.order_by('-name')
        context['subcategories'] = SubCategory.objects.all().select_related('category')
        context['products'] = Products.objects.all()
        context['images'] = Images.objects.filter(is_main=True)
        return context



def sub_category_pages(request, cat_slug, sub_cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    subcategory = get_object_or_404(SubCategory, slug=sub_cat_slug)
    categorys = Category.objects.order_by('-name')
    subcategorys = SubCategory.objects.all()
    products = Products.objects.all()
    images = Images.objects.filter(is_main=True)
    context = {'categories_slug': category, 'subcategories_slug': subcategory, 
               'categories': categorys, 'subcategories': subcategorys, 
               'images': images, 'products': products}

    return render(request, "main_pages/sub-category.html", context)


def products_card(request, cat_slug, sub_cat_slug, product_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    subcategory = get_object_or_404(SubCategory, slug=sub_cat_slug)
    product_slug = get_object_or_404(Products, slug=product_slug)
    categorys = Category.objects.order_by('-name')
    subcategorys = SubCategory.objects.all()
    products = Products.objects.all()
    images = Images.objects.all()
    context = {'categories_slug': category,
               'subcategories_slug': subcategory,
               'product_slug': product_slug, 
               'categories': categorys, 'subcategories': subcategorys, 'images': images, 
               'products': products}
    return render(request, 'main_pages/product.html', context=context)











