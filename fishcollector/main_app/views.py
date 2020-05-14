from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Fish, Food
from .forms import FeedingForm



def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def fishes_index(request):
  fishes = Fish.objects.filter(user=request.user)
  return render(request, 'fishes/index.html', {'fishes': fishes})   

@login_required
def fishes_detail(request, fish_id):
  fish = Fish.objects.get(id=fish_id)
  foods_fish_doesnt_have = Food.objects.exclude(id_in = fish.foods.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'fishes/detail.html', {
     'fish': fish,
     'feeding_form': feeding_form,
     'foods': foods_fish_doesnt_have
     })

@login_required
def add_feeding(request, fish_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.fish_id = fish_id
    new_feeding.save()
  return redirect('cats_detail', fish_id=fish_id)          

class FishCreate(LoginRequiredMixin, CreateView):
  model = Fish
  fields = '__all__'  
  success_url = '/fishes/'

  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class FishUpdate(LoginRequiredMixin, UpdateView):
  model = Fish
  fields = ['size', 'description', 'age']

class FishDelete(LoginRequiredMixin, DeleteView):
  model = Fish
  success_url = '/fishes/'  

@login_required
def assoc_food(request, fish_id, food_id):
  Food.objects.get(id=fish_id).foods.add(food_id)
  return redirect('detail', fish_id=fish_id)

@login_required
def unassoc_food(request, fish_id, food_id):
  Fish.objects.get(id=fish_id).foods.remove(food_id)
  return redirect('detail', fish_id=fish_id)

class FoodList(LoginRequiredMixin, ListView):
  model = Food

class FoodDetail(LoginRequiredMixin, DetailView):
  model = Food

class FoodCreate(LoginRequiredMixin, CreateView):
  model = Food
  fields = '__all__'

class FoodUpdate(LoginRequiredMixin, UpdateView):
  model = Food
  fields = ['name', 'brand']

class FoodDelete(LoginRequiredMixin, DeleteView):
  model = Food
  success_url = '/foods/'      

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)  