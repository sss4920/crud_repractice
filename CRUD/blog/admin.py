from django.contrib import admin
from .models import Article, Comment #blog.models 해도됨
# Register your models here.

admin.site.register(Article)
admin.site.register(Comment)