from pdb import post_mortem
from django.contrib import admin
from .models import Post, Comment


admin.site.register(Post)
admin.site.register(Comment)
