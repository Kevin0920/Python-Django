from django.conf.urls import url

# controller!!!!

from . import views           # This line is new!
urlpatterns = [
	url(r'^$', views.index)     # This line has changed!
	]