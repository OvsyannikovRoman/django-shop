from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello WORLD!!!")

from django.http import HttpResponse
from .models import Category

def index(request):
    categories = Category.objects.all()
    # Собираем все названия категорий в одну строку через запятую или пробел
    response_text = '<br>'.join([str(category) for category in categories])
    return HttpResponse(response_text)