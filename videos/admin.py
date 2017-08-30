# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Video


class VideoAdmin(admin.ModelAdmin):
    list_filter = ['updated', 'time_stamp']
    list_display = ['title', 'updated', 'time_stamp']
    readonly_fields = ['updated', 'time_stamp', 'short_title']
    search_fields = ['title', 'embed_code']

    class Meta:
        model = Video

    @staticmethod
    def short_title(obj):
        return obj.title[:3]


# Register your models here.
admin.site.register(Video, VideoAdmin)
