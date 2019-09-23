from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import RegisterForm, LoginForm


def index(request):
    return render(request, 'index.html', {
        'email': request.session.get('user')  # LoginView에서 form_valid가 끝날경우 session을 넘겨준다.
    })


# 회원가입
class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'  # 어떤 주소로 이동 시킬때


# 로그인
class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    # 유효성 검사가 끝났을때, 모든 데이터가 정상적일때 (로그인 데이터가 정상적일때) 들어오는 함수
    def form_valid(self, form):
        self.request.session['user'] = form.email
        return super().form_valid(form)


# 로그아웃
def logout(request):
    if 'user' in request.session:
        del (request.session['user'])

    return redirect('/')
