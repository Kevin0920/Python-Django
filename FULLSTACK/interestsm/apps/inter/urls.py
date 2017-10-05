from django.conf.urls import url
from . import views  # This line is new!

urlpatterns = [
    url(r'^$', views.index),  # This line has changed!
    url(r'^submit', views.submit),
    url(r'^users', views.users),
    url(r'^interests/(?P<name>\w+)$', views.interests, name = 'username')
]