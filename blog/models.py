from django.db import models
from account.models import MyUser, User
from django.utils.text import slugify
from tinymce import models as tinymce_models
from bs4 import BeautifulSoup
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=60, unique=True, blank=True)
    description = tinymce_models.HTMLField()
    date = models.CharField(max_length=255, default="15 November 2020")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save()

    def get_absolute_url(self, *args, **kwargs):
        return reverse('category', kwargs={'slug':self.slug})

class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=60, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    thumbnail = models.FileField(upload_to='blog/post', null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save()

    def get_absolute_url(self, *args, **kwargs):
        return reverse('subcategory', kwargs={'slug':self.slug})



class Post(models.Model):
    statuses = [
        ('D', 'Draft'),
        ('P', 'Publish')
    ]
    title = models.CharField(max_length=120)
    slug = models.CharField(max_length=60, unique=True, blank=True)
    content = tinymce_models.HTMLField()
    status = models.CharField(max_length=1, choices=statuses)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    grade = models.CharField(max_length=120, default="student name", blank=True)
    thumbnail = models.FileField(upload_to='blog/post/thumbnail', null=True, blank=True)
    files = models.FileField(upload_to='blog/post', null=True, blank=True)
    video_or_not = models.BooleanField(default=False)
    date = models.DateField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='blog_likes')

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save()

    def get_absolute_url(self, *args, **kwargs):
        return reverse('post-update', kwargs={'slug':self.slug})

    def html_to_text(self, *args, **kwargs):
        soup = BeautifulSoup(self.content, features="html.parser")
        text = soup.get_text()
        return text
