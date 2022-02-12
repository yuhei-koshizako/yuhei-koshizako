
from django.contrib import admin
from django.urls import path

from blog.views import frontpage, post_deteil

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",frontpage),
    path("<slug:slug>/", post_deteil, name="post_detail")
]
