from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Categories

# Create your views here.
def index(request):

    context = {
        "title": "Home - Главная",
        "content": "Магазин мебели HOME",
    }

    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "Home - О нас",
        "content": "О нас",
        "text_on_page": "Text classsni ochen mnogo"
    }
    return render(request, "main/about.html", context)
