from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^wjcontact/$', views.contact_list, name='wjcontact_list'),
    url(r'^wjcontact/(?P<pk>\d+)/$', views.contact_detail, name='wjcontact_detail'),
    url(r'^wjcontact/new/$', views.contact_new, name='wjcontact_new'),
    url(r'^wjcontact/(?P<pk>\d+)/contact/$', views.contact_edit, name='wjcontact_edit'),
    url(r'^wjcontact/delete/(?P<pk>\d+)/$', views.contact_delete, name='wjcontact_delete'),
]