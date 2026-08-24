from django.shortcuts import render
from django.http import HttpResponse
from goods.models import Category


def index(request):
    category = Category.objects.all()

    context = {
        "title": "Main page - Home",
        "content": "Furniture Shop",
        "categories": category
    }

    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "About Us - Home",
        "content": "About Us",
        "text_on_page": "Text about why this shop is good"
    }

    return render(request, "main/about.html", context)