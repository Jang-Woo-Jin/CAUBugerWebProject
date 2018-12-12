from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('introduction/', views.introduction, name='introduction'),
    path('order/', views.order, name='order'),
    path('seats/', views.seats, name='seats'),
    path('notice/', views.notice, name='notice'),
    path('signup/', views.signup, name='signup'),
    path('changepw/', views.changepw, name='changepw'),
    
    url('^', include('django.contrib.auth.urls')),
]