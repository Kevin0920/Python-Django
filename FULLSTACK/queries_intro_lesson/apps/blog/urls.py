from django.conf.urls import url, include
# from django.contrib import admin
from . import views
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name = 'index'),
    url(r'^blogs$', views.blogs),
    url(r'^comments/(?P<id>\d+)$', views.comments),
]
