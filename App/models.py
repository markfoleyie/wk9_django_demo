from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"
    name = models.CharField(max_length=50)
    hashtag = models.CharField(max_length=20)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name


class Post(models.Model):
    class Meta:
        verbose_name_plural = "Posts"
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    @property
    def as_dict(self):
        return {
            "title": self.title,
            "content": self.content,
            "category": f"{self.category}",
            "owner": f"{self.owner}"
        }
