import json
import os

from django.shortcuts import render

MODULE_DIR = os.path.dirname(__file__)


def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    file_path = os.path.join(MODULE_DIR, 'fixtures/products.json')
    context = {
        'title': 'GeekShop - Каталог',
        'sections' : ['Новинки', 'Одежда', 'Обувь', 'Аксессуары', 'Подарки'],
        'goods': [i['fields'] for i in json.load(open(file_path, encoding='utf-8'))]
    }
    return render(request, 'mainapp/products.html', context)
