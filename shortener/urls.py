from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_view),
    url(r'^create', views.create_view, name='main_view'),
    url(r'^(?P<url>\w+)/$', views.shorturl_view),
]
