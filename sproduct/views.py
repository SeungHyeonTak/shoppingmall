from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Product
from .forms import RegisterForm
from sorder.forms import RegisterForm as OrderForm  # order안에 forms로 명령


class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product_list'  # templates에서 기본적으로 사용되는 object_list를 사용하기 싫을때 사용함


class ProductCreate(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = '/product/'


class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    queryset = Product.objects.all()
    context_object_name = 'product'

    def get_context_data(self, **kwargs):  # DetailView에다가 별도로 form을 만드는데 원하는 데이터를 넣을 수 있도록 함수 제공
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm(self.request)
        return context
