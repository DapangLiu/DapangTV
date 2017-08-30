# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .models import Course
from .forms import CourseForm
from videos.mixins import MemberRequiredMixin, StaffMemberRequired


# Create Video
class CourseCreateView(CreateView, StaffMemberRequired):
    model = Course
    form_class = CourseForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(CourseCreateView, self).form_valid(form)


# Video Detail
class CourseDetailView(MemberRequiredMixin, DetailView):
    queryset = Course.objects.all()

    # 解决重复问题
    def get_object(self):
        obj = Course.objects.filter(slug=self.kwargs.get("slug"))
        if obj.exists():
            return obj.first()
        raise Http404


# Video List
class CourseListView(ListView):
    def get_queryset(self):
        request = self.request
        queryset = Course.objects.all()
        query = request.GET.get("q")
        if query:
            queryset = queryset.filter(title__icontains=query)
        return queryset


# Video Update
class CourseUpdateView(UpdateView, StaffMemberRequired):
    queryset = Course.objects.all()
    form_class = CourseForm

    # 解决重复问题
    def get_object(self):
        obj = Course.objects.filter(slug=self.kwargs.get("slug"))
        if obj.exists():
            return obj.first()
        raise Http404


# Video Delete
class CourseDeleteView(DeleteView, StaffMemberRequired):
    queryset = Course.objects.all()
    success_url = '/videos/'

    # 解决重复问题
    def get_object(self):
        obj = Course.objects.filter(slug=self.kwargs.get("slug"))
        if obj.exists():
            return obj.first()
        raise Http404
