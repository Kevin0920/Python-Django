from django.conf.urls import url, include
# from django.contrib import admin

from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^projects$', views.projects),
    url(r'^about$', views.about),
    url(r'^testimotionals$', views.testimotionals),
    url(r'^search$', views.search),
]
