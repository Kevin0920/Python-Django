from django.conf.urls import url, include

from . import views


urlpatterns = [
    url(r'^$', views.index),
    # url(r'^posts$', views.post, name='posts'),


    url(r'^add$', views.addNote),
    url(r'^delnote/(?P<id>\d+)$', views.delnote),
    url(r'^', views.index),
]
