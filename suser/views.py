from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegisterForm


def index(request):
    return render(request, 'index.html')


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/' # 어떤 주소로 이동 시킬때
