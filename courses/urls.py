"""DapangTV URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from courses.views import (CourseListView,
                          CourseDetailView,
                          CourseCreateView,
                          CourseUpdateView,
                          CourseDeleteView,
                          LectureDetailView,
                          )

urlpatterns = [
    url(r'^$', CourseListView.as_view(), name='list'),
    url(r'^create/', CourseCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', CourseDetailView.as_view(), name='detail'),
    url(r'^(?P<cslug>[\w-]+)/(?P<lslug>[\w-]+)/$', LectureDetailView.as_view(), name='lecture-detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', CourseUpdateView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', CourseDeleteView.as_view(), name='delete'),
]
