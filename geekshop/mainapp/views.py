import json

from django.shortcuts import render


def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    with open('mainapp/fixtures/products.json', 'r', encoding='utf-8') as f:
        goods = json.loads(f.read())
    context = {
        'title': 'GeekShop - Каталог',
        'goods': goods
    }
    return render(request, 'mainapp/products.html', context)
