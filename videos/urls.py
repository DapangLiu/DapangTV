from django.conf.urls import url, include
from django.contrib import admin

from videos.views import (VideoListView,
                          VideoDetailView,
                          VideoCreateView,
                          VideoUpdateView,
                          VideoDeleteView,
                          )

urlpatterns = [
    url(r'^$', VideoListView.as_view(), name='list'),
    url(r'^create/$', VideoCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', VideoDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', VideoUpdateView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', VideoDeleteView.as_view(), name='delete'),
]
