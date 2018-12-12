from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('introduction/', views.introduction, name='introduction'),
    path('order/<int:listnum>', views.order, name='order'),
    path('oreder/detail/<int:pk>', views.orderdetail, name='order specific'),
    path('seats/', views.seats, name='seats'),
    path('notice/<int:listnum>', views.notice, name='notice'),
    path('notice/detail/<int:pk>', views.noticedetail, name='notice specific'),
    path('signup/', views.signup, name='signup'),
    path('changepw/', views.changepw, name='changepw'),
    
    url('^', include('django.contrib.auth.urls')),
]