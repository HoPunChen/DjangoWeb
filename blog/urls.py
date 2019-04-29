# -*- coding: utf-8 -*- 
__author__ = 'HoPun'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]