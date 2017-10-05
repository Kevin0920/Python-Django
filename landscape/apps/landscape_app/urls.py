from django.conf.urls import url, include
# from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<id>[0-9]+)$', views.idroute),
    url(r'^', views.error),
]
