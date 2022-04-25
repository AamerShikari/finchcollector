from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Finch
# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def finch_index(request): 
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})