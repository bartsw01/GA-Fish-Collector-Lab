from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('fishes/', views.fishes_index, name='index'),
  path('fishes/<int:pk>/', views.fishes_detail, name='detail'),
  path('fishes/create/', views.FishCreate.as_view(), name='fishes_create'),
  path('fishes/<int:pk>/update/', views.FishUpdate.as_view(), name='fishes_update'),
  path('fishes/<int:pk>/delete/', views.FishDelete.as_view(), name='fishes_delete'),
  path('fishes/<int:pk>/add_feeding', views.add_feeding, name='add_feeding'),
  path('fishes/<int:fish_id>/assoc_food/<int:food_id>/', views.assoc_food, name='assoc_food'),
  path('fishes/<int:fish_id>/unassoc_food/<int:food_id>/', views.unassoc_food, name='unassoc_food'),
  path('foods/', views.FoodList.as_view(), name='foods_index'),
  path('foods/<int:pk>/', views.FoodDetail.as_view(), name='foods_detail'),
  path('foods/create/', views.FoodCreate.as_view(), name='foods_create'),
  path('foods/<int:pk>/update/', views.FoodUpdate.as_view(), name='foods_update'),
  path('foods/<int:pk>/delete/', views.FoodDelete.as_view(), name='foods_delete'),
]