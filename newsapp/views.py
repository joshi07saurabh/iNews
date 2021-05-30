from django.shortcuts import render, resolve_url
import requests
from requests.api import request
API_KEY = '8ebfb70aa43048bd89fd25cb1ae84aa2'

# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    country = request.GET.get("country")
    category = request.GET.get("category")
    
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    context = {'articles':articles}
    return render(request,'home.html',context)