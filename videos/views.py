# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .models import Video
from .forms import VideoForm
from .mixins import MemberRequiredMixin, StaffMemberRequired


# Create Video
class VideoCreateView(CreateView, StaffMemberRequired):
    model = Video
    form_class = VideoForm


# Video Detail
class VideoDetailView(MemberRequiredMixin, DetailView):
    queryset = Video.objects.all()

    def get_object(self):
        return get_object_or_404(Video, slug=self.kwargs.get("slug"))


# Video List
class VideoListView(ListView):
    def get_queryset(self):
        request = self.request
        queryset = Video.objects.all()
        query = request.GET.get("q")
        if query:
            queryset = queryset.filter(title__icontains=query)
        return queryset


# Video Update
class VideoUpdateView(UpdateView, StaffMemberRequired):
    queryset = Video.objects.all()
    form_class = VideoForm


# Video Delete
class VideoDeleteView(DeleteView, StaffMemberRequired):
    queryset = Video.objects.all()
    success_url = '/videos/'
