from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Add the Cat class & list and view function below the imports
class Fish:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, size, description, age):
    self.name = name
    self.size = size
    self.description = description
    self.age = age

fishes = [
  Fish('Tilapia', '2 lbs', 'freshwater food fish', 3),
  Fish('Blue Gill', '3-4 lbs', 'deep blue purple on face', 2),
  Fish('Trout', '10 lbs', 'spotted rainbow trout', 4)
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def fishes_index(request):
    return render(request, 'fishes/index.html', {'fishes': fishes})    