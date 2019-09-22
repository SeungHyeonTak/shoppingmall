from django.shortcuts import render
from django.views.generic import ListView
from .models import Product


class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product_list'  # templates에서 기본적으로 사용되는 object_list를 사용하기 싫을때 사용함
