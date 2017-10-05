from django.conf.urls import url, include
# from django.contrib import admin
from . import views
urlpatterns = [
    url( r'^$', views.index ),

    url( r'^login$', views.login, name="login" ),
    url( r'^reg$', views.reg, name="reg" ),

    url( r'^secrets$', views.secrets, name="secrets" ),
    url( r'^secrets/top$', views.top, name="top" ),

    url( r'^like/(?P<id>\d+)$', views.like, name="like" ),

    url( r'^logout$', views.logout, name="logout" ),

    url( r'^deluser/(?P<id>\d+)$', views.deluser, name="deluser" ),
    url( r'^delsecret/(?P<id>\d+)$', views.delsecret, name="delsecret" ),
]
