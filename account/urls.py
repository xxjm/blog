
from django.urls import path, include
from . import views

app_name="account"
urlpatterns = [
   path('zhuce/', views.zhuce, name='页面'),
   path('login/', views.login, name='登陆'),
   path('logout/', views.logout, name='登出'),
   path('signin/', views.signin, name='注册'),
]