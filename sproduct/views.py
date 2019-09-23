from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from suser.decorators import admin_required
from .models import Product
from .forms import RegisterForm
from sorder.forms import RegisterForm as OrderForm  # order안에 forms로 명령
from rest_framework import generics, mixins
from .serializers import ProductSerializer


class ProductListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProductDetailAPI(generics.GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product_list'  # templates에서 기본적으로 사용되는 object_list를 사용하기 싫을때 사용함


@method_decorator(admin_required, name='dispatch')
class ProductCreate(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = '/product/'

    def form_valid(self, form):
        product = Product(
            name=form.data.get('name'),
            price=form.data.get('price'),
            description=form.data.get('description'),
            stock=form.data.get('stock')
        )
        product.save()
        return super().form_valid(form)  # 오버라이딩을 했기에 부모에 있는 함수를 호출해줘야한다.


class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    queryset = Product.objects.all()
    context_object_name = 'product'

    def get_context_data(self, **kwargs):  # DetailView에다가 별도로 form을 만드는데 원하는 데이터를 넣을 수 있도록 함수 제공
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm(self.request)
        return context
