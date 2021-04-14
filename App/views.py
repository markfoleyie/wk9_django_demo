from django.shortcuts import render
from django.http import JsonResponse
from . import models


# Create your views here.

def list_posts(request):
    posts = models.Post.objects.all()

    returning_json = {"posts": []}
    for post in posts:
        returning_json["posts"].append(post.as_dict)

    return JsonResponse(returning_json, status=200)
