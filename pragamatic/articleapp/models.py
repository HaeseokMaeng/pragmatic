from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Article(models.Model) :
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True)

    title = models.CharField(max_length=200, null=True)
    img = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)

    create_at = models.DateField(auto_now=True, null=True)


class Favorite(models.Model) :
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='favorite', null=True)
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, related_name='favorite', null=True)
