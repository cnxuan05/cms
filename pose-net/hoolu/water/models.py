# coding:utf-8
from django.db import models
from django.contrib.auth.models import User, AbstractUser


# class User(AbstractUser):
#     desc = models.TextField()

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    desc = models.TextField(blank=True, null=True)


# Create your models  here.
class Publisher(models.Model):
    name = models.CharField(max_length=30, verbose_name='名称')
    address = models.CharField("地址", max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        verbose_name = '出版商'
        verbose_name_plural = '出版商'

    def __unicode__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = '作者'
        verbose_name_plural = '作者'


class AuthorDetail(models.Model):
    sex = models.BooleanField(max_length=1, choices=((0, '男 '), (1, '女')))
    email = models.EmailField()
    address = models.CharField(max_length=50)
    birthday = models.DateField()
    author = models.OneToOneField(Author)

    class Meta:
        verbose_name = '作者详情'
        verbose_name_plural = '作者详情'


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    class Meta:
        verbose_name = '书籍'

        verbose_name_plural = '书籍'

    pass


class News(models.Model):
    list_fields = ['id', 'new_thread', 'new_title', 'new_url', 'new_time', 'new_form', 'from_url', 'news_body']
    new_thread = models.TextField(blank=True, null=True)
    new_title = models.TextField(blank=True, null=True)
    new_url = models.TextField(blank=True, null=True)
    new_time = models.TextField(blank=True, null=True)
    new_form = models.TextField(blank=True, null=True)
    from_url = models.TextField(blank=True, null=True)
    news_body = models.TextField(blank=True, null=True)
    dele = models.BooleanField(default=0)

    def __str__(self):
        return models.Model.__str__(self)

    class Meta:
        permissions = (('can_view', 'Can see news'),
                       ('can_add', 'Can add news'),
                       ('can_edit', 'Can see news'),
                       ('can_delete', 'Can delete news'),
                       )
