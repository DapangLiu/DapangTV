from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from django.db.models.signals import pre_save
from .utils import create_slug
from videos.models import Video


class Course(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    slug = models.SlugField(blank=True, unique=True)
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=100)
    updated = models.DateTimeField(auto_now=True)  # last save
    time_stamp = models.DateTimeField(auto_now_add=True)  # time added

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return "/videos/{slug_arg}/".format(slug_arg=self.slug)
        return reverse("courses:detail", kwargs={"slug": self.slug})


class Lecture(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    video = models.ForeignKey(Video, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(blank=True, unique=True)
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    updated = models.DateTimeField(auto_now=True)  # last save
    time_stamp = models.DateTimeField(auto_now_add=True)  # time added

    def __str__(self):
        return self.title

    class Meta:
        unique_together = (('slug', 'course'), )

    def get_absolute_url(self):
        # return "/videos/{slug_arg}/".format(slug_arg=self.slug)
        return reverse("courses:lecture-detail", kwargs={
            "cslug": self.course.slug,
            "lslug": self.slug,
        })


def pre_save_receiver(sender, instance, *args, **kwargs):
    instance.slug = create_slug(instance)


pre_save.connect(pre_save_receiver, sender=Course)
# pre_save.connect(pre_save_receiver, sender=Lecture)
