from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch, Feeding
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

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'
    success_url = '/finches'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'