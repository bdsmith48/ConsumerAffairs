from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.write_review, name='write_review'),
    url(r'^index/$', views.index, name='index'),
    url(r'^(?P<review_id>[0-9]+)/$', views.detail, name='detail'),
]
