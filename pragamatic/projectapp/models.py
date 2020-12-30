from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Project(models.Model) :
    title = models.CharField(max_length=20, null=True)
    description = models.CharField(max_length=250, null=True)
    img = models.ImageField(upload_to='project/', null=False)
    create_at = models.DateField(auto_now=True, null=True)
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='project', null=True)
