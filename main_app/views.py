from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch, Feeding, Toy
from .forms import FeedingForm
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
    feeding_form = FeedingForm()
    return render(request, 'finches/details.html', {'finch': finch, 'feeding_form': feeding_form})

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

def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)

def toys(request):
    toys = Toy.objects.all()
    return render(request, 'toys/index.html', {'toys': toys})