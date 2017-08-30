from django.contrib import admin

# Register your models here.
from .models import Course, Lecture


class LectureInLine(admin.TabularInline):
    model = Lecture
    # 以下代码能确保 同一个 course 下的 videos 不能重名
    # 但是不同 course 下的 video 可以重名
    prepopulated_fields = {"slug": ("title",)}
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    inlines = [LectureInLine]
    list_filter = ['updated', 'time_stamp']
    list_display = ['title', 'updated', 'time_stamp']
    readonly_fields = ['updated', 'time_stamp', 'short_title']
    search_fields = ['title', 'description']

    class Meta:
        model = Course

    @staticmethod
    def short_title(obj):
        return obj.title[:3]


admin.site.register(Course, CourseAdmin)