from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('title', )
        verbose_name_plural = 'Categories'

    def __unicode__():
        return self.title


class Article(models.Model):
    DRAFT = 1
    PUBLISHED = 2
    STATUS_CHOICES = (
            (DRAFT, 'Draft'),
            (PUBLISHED, 'Published'),
        )

    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT)
    published_date = models.DateField(default=datetime.now)
    modified_date = models.DateField(auto_now=True)
    category = models.ForeignKey(Category)
    author = models.ForeignKey(User)
    image = models.ImageField(upload_to='raw')

    class Meta:
        ordering = ('published_date', )

    def __unicode__(self):
        return self.title
