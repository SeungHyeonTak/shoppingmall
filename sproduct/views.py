from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .models import Product
from .forms import RegisterForm


class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product_list'  # templates에서 기본적으로 사용되는 object_list를 사용하기 싫을때 사용함


class ProductCreate(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = '/product/'