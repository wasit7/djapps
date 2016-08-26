from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^signin/', views.signin, name='signin'),
	url(r'^signout/', views.signout, name='signout'),
	url(r'^home/', views.home, name='home'),
]