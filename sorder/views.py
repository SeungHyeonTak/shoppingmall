from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.db import transaction
from suser.decorators import login_required
from .forms import RegisterForm
from .models import Order
from sproduct.models import Product
from suser.models import User
from rest_framework import generics, mixins
from .serializers import OrderSerializer


class OrderListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    """
    쇼핑몰 주문 목록의 데이터를 불러오는 API

    ---
    # 내용
        - user : 사용
        - product : 상품
        - quantity : 수량
        - register_date : 등록날짜
    """
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class OrderCreate(FormView):
    form_class = RegisterForm
    success_url = '/product/'

    def form_valid(self, form):
        with transaction.atomic():
            prod = Product.objects.get(pk=form.data.get('product'))
            order = Order(
                quantity=form.data.get('quantity'),
                product=prod,
                user=User.objects.get(email=self.request.session.get('user'))
            )
            order.save()
            prod.stock -= int(form.data.get("quantity"))
            prod.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        return redirect('/product/' + str(form.data.get('product')))

    def get_form_kwargs(self, **kwargs):  # form을 생성할때 어떤 인자값을 전달해서 만들건지 결정하는 함수
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw


@method_decorator(login_required, name='dispatch')
class OrderList(ListView):
    template_name = 'order.html'
    context_object_name = 'order_list'

    # 현재 로그인한 사용자의 데이터만 가져온다.
    def get_queryset(self, **kwargs):  # 함수로 오버라이딩
        querset = Order.objects.filter(user__email=self.request.session.get('user'))
        # user__email = 사용자의 이메일
        return querset
