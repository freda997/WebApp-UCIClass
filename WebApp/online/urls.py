
from django.conf.urls import url, include
from django.contrib import admin
from online import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^login/$', views.login, name='login'),
    url(r'^regist/$', view.regist, name='regist'),
    url(r'^index$', view.index, name='index'),
    url(r'^logout/$', views.logout, name='logout')
    ]