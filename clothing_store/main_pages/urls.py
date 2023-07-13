from django.urls import path 
from . import views 
urlpatterns = [
    path('', views.MainPageCategory.as_view(), name='home'),
    path('category/catalog/', views.Catalog.as_view(), name='catalog'),
    path('category/<slug:cat_slug>/', views.CategoryPages.as_view()   ,name='category'),
    path("category/<slug:cat_slug>/<slug:sub_cat_slug>/", views.sub_category_pages, name='sub_category'), 
    path("category/<slug:cat_slug>/<slug:sub_cat_slug>/<slug:product_slug>/", views.products_card, name='product_card')

]