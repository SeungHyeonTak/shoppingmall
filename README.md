# 쇼핑몰 개발 구현(연습)* 프로젝트 생성  * project name : config  * project app : suser / sproduct / sorder  * 가상환경 (venv)* python version : 3.6.8* Django version : 2.2.5* Datebase : sqlite3*****#### 참고* 따로 기본구성 연습용이라 배포는 하지않음* CBV(Class Based View)로 연습* Django REST Framework(DRF) 공부 목적으로 생성* REST API 부분 중심으로 갈거라 template부분에 대한 설명은 건너 뜀*****#### 프로젝트 내용* suser(회원가입) - url(/register)  * class view로 설계하고 forms.py로 회원가입 구현    * generic.edit - FormView 활용    * 이메일 / 비밀번호 / 비밀번호 확인 입력란 (form)    * 비밀번호 / 비밀번호 확인 부분 일치 불일치 구현 (form)    * admin site에 회원가입된 정보 확인    * suser(로그인) - url(/login)  * 회원가입과 비슷한 형태로 CBV 작성  * LoginForm으로 email과 password의 유효성 검사  * LoginView에서 데이터가 정상적이면 form_valid로 session으로 넘겨줌 * sproduct(상품 목록) - url(/product)  * 간단하게 generic의 ListView 사용  * context_object_name으로 queryset name 변경 가능  * templates부분에서 humanize의 filter처리 (intcomma / date:'Y-m-d H:i')* sproduct(상품 등록) - url(/product/create)  * FormView를 사용하며, forms.py를 활용하여 저장시킨다.  * 상품 설명 부분(description) summernote로 WYSIWYG 구현* sproduct(상품 상세보기) - url(/product/detail)  * views의 generic - DetailView사용  * transaction을 사용해 단위작업 구현  * 항상 오타 조심하기  * sorder(주문정보 조회) - url(/order)  * 현재 로그인한 사용자의 데이터만 가져오게 구현    * get_queryset()으로 함수 오버라이딩    * Decorator  * 함수를 Wrapping을 해서 기능을 재사용 할 수 있는 기법```pythondef login_required(func):    def wrap():        if user is None:            return redirect('/login')        return func()    return wrap()# 위 함수를 사용하여 밑의 함수들을 Decorator로 사용하여 쓸 수 있다.@login_requireddef test_func1():    print('Do something1')    @login_requireddef test_func2():    print('Do something2')```  * decorator로 페이지 권한 설정 하기 (일반사용자/관리자) 별로 나누어서 구현* Form과 Model의 분리  * 깔끔한 처리를 위해 forms.py에서 처리해야 할 부분을 views.py에서 한번에 처리*****#### DRF (Django REST Framework)> 프론트가 백엔드에게 데이터를 요청할때 사용하는게 API> 그중에 REST API가 있는데 리소스를 기반으로 디자인된 API이다.* API가 표시하는 리소스 URL은 동사가 아닌 명사를 기반으로 정해야함```text* https://example.com/order -> (o)* https://example.com/create-order -> (x)```* HTTP 메서드를 기준으로 작업 정의  * GET : 지정된 URL에서 리소스의 표현을 검색(불러온다)  * POST : 지정된 URL에서 새 리소스를 생성(생성한다.)  * PUT : 지정된 URL에 리소스를 만들거나 대체할때 / 업데이트 할때 지정함(해당 데이터 전체 수정)  * PATCH : 리소스 부분의 업데이트를 수행(일부분 수정 할때)  * DELETE : 지정된 URL의 리소스를 제거* Tip : 리소스 URL 항목을 복잡하게 정하지 않는것이 좋다.  * ex) example.com/1/order/1/... 이런식으로 하는건 `비추`  * 실행된 결과는 HTTP 상태 코드로 표시  * GET    * 200(정상) / 404(찾을 수 없음)으로 반환  * POST    * 201(정상) - 새로 생성되어졌다는 뜻이기 때문에    * 200(정상) - 만들지 않았을때    * 204(내용없음) - 반환결과가 없을때    * 400(잘못된 요청)  * PUT    * 201(만들어짐) - 새 리소스를 만들때    * 409(충돌)> 출처 : <https://docs.microsoft.com/ko-kr/azure/architecture/best-practices/api-design'>#### Django REST Framework 설치> $ pip install django-rest-framework* 이후 settings.py -> INSTALLED_APPS에 추가 `rest_framework` * serializers.py 생성 후 Meta class를 이용해 models.py의 값 가져오기* 이후 views.py에서 GenericAPIView와 mixin을 이용해 API 생성  * 자세한 보기는 코드 참조#### Django REST Framework API 문서 자동화> drf-yasg 사용* 패키지 설치  * $ pip install -U drf-yasg    * settings.py - INSTALLED_APPS에 'def_yasg' 추가  * $ pip install flex* redoc / swagger를 사용하여 자동화 API 문서 작성*****#### Django ERD 만들기* Django-extensions를 이용하여 ERD 만들기* $ pip install django-extensions```python# settings.pyINSTALLED_APPS = [    ...    'django_extensions',]GRAPH_MODELS = {    'all_applications': True,    'group_models': True,}```* $ pip install pygraphviz* $ python manage.py graph_models -a -g -o my_project_visualized.png> 이후에는 ERD file이 png로 생성 되어 볼 수 있다.  