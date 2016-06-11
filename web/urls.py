from django.conf.urls import url

from . import views
from . import api

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^regist$', views.regist, name='regist'),
    url(r'^login$', views.login, name='login'),
    url(r'^create$', views.create, name='create'),
    url(r'^submit$', views.submit, name='submit'),
    url(r'^api/login$', api.login, name='login'),
    url(r'^api/regist$', api.regist, name='regist'),
    url(r'^api/logout$', api.logout, name='logout'),
    url(r'^api/submit$', api.submit, name='submit'),
    url(r'^create/(?P<scriptID>[0-9]+)$', views.createID, name='create'),
    url(r'^home$', views.home, name='home'),
    url(r'^index$', views.index, name='index'),
]
