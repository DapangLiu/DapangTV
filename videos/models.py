# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from courses.utils import create_slug


# Create your models here.
class Video(models.Model):
    slug = models.SlugField(blank=True)
    title = models.CharField(max_length=120)
    embed_code = models.TextField()
    free = models.BooleanField(default=True)
    member_required = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)  # last save
    time_stamp = models.DateTimeField(auto_now_add=True)  # time added

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return "/videos/{slug_arg}/".format(slug_arg=self.slug)
        return reverse("videos:detail", kwargs={"slug": self.slug})


def pre_save_receiver(sender, instance, *args, **kwargs):
    instance.slug = create_slug(instance)


pre_save.connect(pre_save_receiver, sender=Video)
