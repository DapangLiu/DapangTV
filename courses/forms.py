from django import forms

from .models import Course, Lecture
from videos.models import Video


class LectureAdminForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = [
            'order',
            'title',
            'video',
            'description',
            'slug',
        ]

    def __init__(self, *args, **kwargs):
        super(LectureAdminForm, self).__init__(*args, **kwargs)
        obj = kwargs.get("instance")
        # 排除已经用过的 Video， 把剩下的显示在列表上
        qs = Video.objects.filter(lecture__isnull=True)
        if obj:
            if obj.video:
                this_ = Video.objects.filter(pk=obj.video.pk)
                qs = (qs | this_)
            self.fields['video'].queryset = qs
        else:
            self.fields['video'].queryset = qs


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'title',
            'slug',
            'description',
            'price',
        ]