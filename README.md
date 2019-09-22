# 쇼핑몰 개발 구현(연습)* 프로젝트 생성  * project name : config  * project app : suser / sproduct / sorder  * 가상환경 (venv)* python version : 3.6.8* Django version : 2.2.5* Datebase : sqlite3*****#### 프로젝트 내용* suser(회원가입) - url(/register)  * class view로 설계하고 forms.py로 회원가입 구현    * generic.edit - FormView 활용    * 이메일 / 비밀번호 / 비밀번호 확인 입력란 (form)    * 비밀번호 / 비밀번호 확인 부분 일치 불일치 구현 (form)    * admin site에 회원가입된 정보 확인    * suser(로그인) - url(/login)  * 회원가입과 비슷한 형태로 CBV 작성  * LoginForm으로 email과 password의 유효성 검사  * LoginView에서 데이터가 정상적이면 form_valid로 session으로 넘겨줌 * sproduct(상품 목록) - url(/product)  * 간단하게 generic의 ListView 사용  * context_object_name으로 queryset name 변경 가능  * templates부분에서 humanize의 filter처리 (intcomma / date:'Y-m-d H:i')* sproduct(상품 등록) - url(/product/create)  * FormView를 사용하며, forms.py를 활용하여 저장시킨다.  * 상품 설명 부분(description) summernote로 WYSIWYG 구현* sproduct(상품 상세보기) - url(/product/detail)  * views의 generic - DetailView사용   *****#### 참고* 따로 기본구성 연습용이라 배포는 하지않음* CBV(Class Based View)로 연습* Django REST Framework(DRF) 공부 목적으로 생성* REST API 부분 중심으로 갈거라 template부분에 대한 설명은 건너 뜀