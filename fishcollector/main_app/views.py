from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Fish, Food
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
  # foods_fish_doesnt_have = Food.objects.exclude(id_in = fish.foods.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'fishes/detail.html', {
     'fish': fish,
     'feeding_form': feeding_form,
    #  'foods': foods_fish_doesnt_have
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

def assoc_food(request, fish_id, food_id):
  Food.objects.get(id=fish_id).foods.add(food_id)
  return redirect('detail', fish_id=fish_id)

def unassoc_food(request, fish_id, food_id):
  Fish.objects.get(id=fish_id).foods.remove(food_id)
  return redirect('detail', food_id=food_id)

class FoodList(ListView):
  model = Food

class FoodDetail(DetailView):
  model = Food

class FoodCreate(CreateView):
  model = Food
  fields = '__all__'

class FoodUpdate(UpdateView):
  model = Food
  fields = ['name', 'brand']

class FoodDelete(DeleteView):
  model = Food
  success_url = '/foods/'      