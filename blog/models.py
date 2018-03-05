from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime


class Bookmark(models.Model):
    title=models.CharField(max_length=20, blank=True, null=True)
    url=models.URLField('url', unique=True)
    pub_date=models.DateTimeField('date published', default=datetime.now, editable=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='북마크'
        verbose_name_plural='북마크 모음'
        ordering=['title',]


        def __str__(self):
            return self.title


class Member(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=40)

    class Meta:
        verbose_name_plural='Member'


# class PublishedManager(models.Manager):
#     def get_queryset(self):
#         return super(PublishedManager, self).get_queryset().filter(status='published')


# class Post(models.Model):
#     objects=models.Manager()
#     publised=PublishedManager()

#     STATUS_CHOICES=(
#         ('draft','Draft'),
#         ('publised','Published'),
#     )