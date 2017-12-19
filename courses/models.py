from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from .utils import create_slug, make_display_price
from videos.models import Video
from .fields import PositionField


class MyCourses(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    courses = models.ManyToManyField('Course', blank=True)
    updated = models.DateTimeField(auto_now=True)  # last save
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.courses.all().count())

    class Meta:
        verbose_name = 'My Courses'
        verbose_name_plural = 'My Courses'


def post_save_user_create(sender, instance, created, *args, **kwargs):
    if created:
        MyCourses.objects.get_or_create(user=instance)


post_save.connect(post_save_user_create, sender=settings.AUTH_USER_MODEL)

POS_CHOICES = (
    ('main', 'Main'),
    ('sec', 'Secondary')
)


class Course(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    slug = models.SlugField(blank=True, unique=True)
    title = models.CharField(max_length=120)
    category = models.CharField(max_length=120, choices=POS_CHOICES, default='main')
    order = PositionField(collection='category')
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=100)
    updated = models.DateTimeField(auto_now=True)  # last save
    time_stamp = models.DateTimeField(auto_now_add=True)  # time added

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return "/videos/{slug_arg}/".format(slug_arg=self.slug)
        return reverse("courses:detail", kwargs={"slug": self.slug})

    def display_price(self):
        return make_display_price(self.price)


class Lecture(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    video = models.ForeignKey(Video, limit_choices_to={'lecture__isnull': False}, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(blank=True, unique=True)
    title = models.CharField(max_length=120)
    order = PositionField(collection='course')
    description = models.TextField(blank=True)
    updated = models.DateTimeField(auto_now=True)  # last save
    time_stamp = models.DateTimeField(auto_now_add=True)  # time added

    def __str__(self):
        return self.title

    class Meta:
        unique_together = (('slug', 'course'), )
        ordering = ['order', 'title'] # 1- 100, title: a - z

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
