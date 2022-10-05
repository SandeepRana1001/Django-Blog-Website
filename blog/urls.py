from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="starting-page"),
    path("all-post", views.post, name="post-page"),
    path("blog/<blog_title>", views.blog, name="blog-page")

]
