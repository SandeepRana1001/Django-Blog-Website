from django.shortcuts import render

# Create your views here.

img_link = {
    "programming-is-great": "https://www.codingem.com/wp-content/uploads/2021/10/juanjo-jaramillo-mZnx9429i94-unsplash-scaled.jpg",
    "mountain-hiking": "https://upload.wikimedia.org/wikipedia/commons/e/e7/Everest_North_Face_toward_Base_Camp_Tibet_Luca_Galuzzi_2006.jpg",
    "nature-at-its-best": "https://media.istockphoto.com/photos/mountain-landscape-picture-id517188688?k=20&m=517188688&s=612x612&w=0&h=i38qBm2P-6V4vZVEaMy_TaTEaoCMkYhvLCysE7yJQ5Q="
}


def index(request):
    return render(request, "blog/index.html")


def post(request):
    return render(request, "blog/post.html")


def blog(request, blog_title):
    return render(request, "blog/blog.html", {
        "blog_title": blog_title.replace('-', ' '),
        "img_url": img_link[blog_title]
    })
