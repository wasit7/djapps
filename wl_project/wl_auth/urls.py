from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.login, name='wl_auth:login'),
	url(r'^home/', views.home, name='home'),
]