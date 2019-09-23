from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import RegisterForm


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
