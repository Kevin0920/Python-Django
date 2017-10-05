from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^', include('apps.first_app.urls')),
    url(r'^$', views.index),
    url(r'^users$', views.show),
    url(r'^', views.error)
]
