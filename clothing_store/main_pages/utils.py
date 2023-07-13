from .models import *
from django.db.models import Count



class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        category = Category.objects.annotate(Count('cat'))
        subcategory = SubCategory.objects.all()
        context['categories'] = category
        context['subcategories'] = subcategory

        return context