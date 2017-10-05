from django.conf.urls import url, include
# from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index ),

    url( r'^books$', views.books ),
    url( r'^books/(?P<id>\d+)$', views.one_book ),
    url( r'^addbookrview$', views.addbookrview, name="addbrview" ),

    url( r'^login$', views.login, name="login" ),
    url( r'^reg$', views.reg, name="reg" ),
    url( r'^logout$', views.logout, name="logout" ),


    url( r'^delbook/(?P<id>\d+)$', views.delbook ),
    url( r'^delreview/(?P<id>\d+)$', views.delreview ),
]
