from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import make_password
from .forms import RegisterForm, LoginForm
from .models import User
from rest_framework import generics, mixins
from .serializers import UserSerializer


class UserListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    """
    쇼핑몰 유저 목록 리스트를 불러오는 API

    ---
    # 내용
        - email : 유저 email
        - password : 비밀번호
        - register_data : 등록날짜
        - level : 등급(user: 일반 유저 / admin: 관리자)
    """
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserDetailAPI(generics.GenericAPIView, mixins.RetrieveModelMixin):
    """
    쇼핑몰 유저의 데이터를 불러오는 API

    ---
    # 내용
        - email : 유저 email
        - password : 비밀번호
        - register_data : 등록날짜
        - level : 등급(user: 일반 유저 / admin: 관리자)
    """
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


def index(request):
    return render(request, 'index.html', {
        'email': request.session.get('user')  # LoginView에서 form_valid가 끝날경우 session을 넘겨준다.
    })


# 회원가입
class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'  # 어떤 주소로 이동 시킬때

    def form_valid(self, form):
        user = User(
            email=form.data.get('email'),
            password=make_password(form.data.get('password')),
            level='user'
        )
        user.save()

        return super().form_valid(form)


# 로그인
class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    # 유효성 검사가 끝났을때, 모든 데이터가 정상적일때 (로그인 데이터가 정상적일때) 들어오는 함수
    def form_valid(self, form):
        self.request.session['user'] = form.data.get('email')
        return super().form_valid(form)


# 로그아웃
def logout(request):
    if 'user' in request.session:
        del (request.session['user'])

    return redirect('/')
