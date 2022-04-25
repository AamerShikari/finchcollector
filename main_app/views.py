from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Finch
# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

# class Finch: 
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age
    


# finches = [
#     Finch ('Tommy', 'Spice Finch', 'Spice finches also referred to as nutmeg and mascot finches are not easy to breed and do not talk or sing much if at all. Still, they are a popular finch pet option among households throughout the world today.', 2),
#     Finch ('Gizell', 'Zebra Finch', 'Zebra finches are arguably the most popular finch pets in existence. They are hardy, resilient, and interactive which are traits loved by kids and adults alike. They can grow up to 4 inches tall and weigh in at about 19 grams when fully matured.', 1),
#     Finch ('Coo', 'Owl Finch', 'These little birds have markings that resemble the owl, hence their name. They have dark bodies, lighter heads, and sometimes some markings on the face and tail.', 0),
# ]


def finch_index(request): 
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})