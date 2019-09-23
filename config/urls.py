"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from suser.views import index, RegisterView, LoginView, logout, UserListAPI, UserDetailAPI
from sproduct.views import ProductList, ProductCreate, ProductDetail, ProductListAPI, ProductDetailAPI
from sorder.views import OrderCreate, OrderList, OrderListAPI
# drf-yasg
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from drf_yasg import openapi

schema_view_v1 = get_schema_view(
    openapi.Info(
        title="Shoppingmall Open API",
        default_version='v1',
        description='Shoppingmall Open API 문서입니다.',
        terms_of_service='https://github.com/SeungHyeonTak',
        contact=openapi.Contact(email='conficker77@gmail.com'),
        license=openapi.License(name='SeungHyeon Tak'),
    ),
    validators=['flex'],
    public=True,
    permission_classes=(AllowAny,),
    # patterns=get
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', logout),
    path('product/', ProductList.as_view()),
    path('product/create/', ProductCreate.as_view()),
    path('product/<int:pk>/', ProductDetail.as_view()),
    path('order/', OrderList.as_view()),
    path('order/create/', OrderCreate.as_view()),

    # API
    path('api/product/', ProductListAPI.as_view()),
    path('api/product/<int:pk>/', ProductDetailAPI.as_view()),
    path('api/user/', UserListAPI.as_view()),
    path('api/user/<int:pk>/', UserDetailAPI.as_view()),
    path('api/order/', OrderListAPI.as_view()),

    # drf-yasg
    # redoc / swagger
    path('redoc/v1/', schema_view_v1.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
    path('swagger(?P<format>\.json|\.yaml)/v1/', schema_view_v1.with_ui(cache_timeout=0), name='schema-json'),
    path('swagger/v1/', schema_view_v1.with_ui('swagger', cache_timeout=0), name='schema-swagger-v1'),
]
