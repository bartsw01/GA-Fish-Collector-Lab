from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Fish
from .forms import FeedingForm



def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def fishes_index(request):
  fishes = Fish.objects.all()
  return render(request, 'fishes/index.html', {'fishes': fishes})   

def fishes_detail(request, pk):
  fish = Fish.objects.get(id=pk)
  feeding_form = FeedingForm()
  return render(request, 'fishes/detail.html', {
     'fish': fish,
     'feeding_form': feeding_form
     })

def add_feeding(request, fish_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.fish_id = pk
    new_feeding.save()
  return redirect('cats_detail', pk=pk)          

class FishCreate(CreateView):
  model = Fish
  fields = '__all__'  
  success_url = '/fishes/'

class FishUpdate(UpdateView):
  model = Fish
  fields = ['size', 'description', 'age']

class FishDelete(DeleteView):
  model = Fish
  success_url = '/fishes/'  