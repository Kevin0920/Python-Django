from django.conf.urls import url, include
# from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^ninjas/$', views.ninjas),
    url(r'^ninjas/(?P<color>[a-z]+)$', views.colorpicked),
    # url(r'^ninjas/orange$', views.michelangelo),
    # url(r'^ninjas/red$', views.raphael),
    # url(r'^ninjas/purple$', views.donatello),
    # url(r'^ninjas/', views.granny),
]
