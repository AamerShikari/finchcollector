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

def finch_details(request, finch_id): 
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/details.html', {'finch': finch})