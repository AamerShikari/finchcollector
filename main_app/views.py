from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
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
    toys_finch_doesnt_have = Toy.objects.exclude(id__in = finch.toys.all().values_list('id'))
    return render(request, 'finches/details.html', {'finch': finch, 'feeding_form': feeding_form, 'toys': toys_finch_doesnt_have})

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

class ToyDetails(DetailView):
    model = Toy

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'
    success_url = '/toys'

class ToyUpdate(UpdateView):
    model = Toy
    fields = ['material', 'color']

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys'

def assoc_toy(request, finch_id, toy_id):
    Finch.objects.get(id=finch_id).toys.add(toy_id)
    return redirect('detail', finch_id=finch_id)