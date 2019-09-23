from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import RegisterForm
from .models import Order


class OrderCreate(FormView):
    form_class = RegisterForm
    success_url = '/product/'

    def form_invalid(self, form):
        return redirect('/product/' + str(form.product))

    def get_form_kwargs(self, **kwargs):  # form을 생성할때 어떤 인자값을 전달해서 만들건지 결정하는 함수
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw


class OrderList(ListView):
    template_name = 'order.html'
    context_object_name = 'order_list'

    # 현재 로그인한 사용자의 데이터만 가져온다.
    def get_queryset(self, **kwargs):  # 함수로 오버라이딩
        querset = Order.objects.filter(user__email=self.request.session.get('user'))
        # user__email = 사용자의 이메일
        return querset
