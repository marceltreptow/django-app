from django.urls import path
from . import views

urlpatterns = [
    path('dogs/', views.get_all_dogs, name="get_all_dogs" ),
    path('dogs/<int:id>/', views.dog_detail, name="get_dog_detail"),
    path('dogs/delete/<int:id>/', views.delete_dog, name="delete_dog"),
    path('dogs/update/<int:id>/', views.alter_dog, name="alter_dog"),
    path('', views.home, name="home"),
    path('dogs/add/', views.form, name="add_dog"),
]
