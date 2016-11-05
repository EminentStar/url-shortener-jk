from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_view),
    url(r'^create', views.create, name='main_view'),
    url(r'^shorturl/(?P<url>\w+)/$', views.shorturl),
]
