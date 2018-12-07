from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('introduction/', views.introduction, name='introduction'),
    path('order/', views.order, name='order'),
    path('seats/', views.seats, name='seats'),
    path('notice/', views.notice, name='notice'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('searchpw/', views.searchpw, name='searchpw'),
    path('changepw/', views.changepw, name='changepw'),
]