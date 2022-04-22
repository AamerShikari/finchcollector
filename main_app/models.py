from django.db import models

# Create your models here.
class Finch: 
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age
    