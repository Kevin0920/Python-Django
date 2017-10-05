from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^loginreg$', views.loginreg),

    url(r'^logout$', views.logout),

    url( r'^deluser/(?P<id>\d+)$', views.deluser, name="deluser" ),
]
