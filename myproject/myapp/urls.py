from django.urls import path
from . import views

urlpatterns = [
    path('dogs/', views.get_all_dogs, name="get_all_dogs" ),
    path('dogs/<int:id>/', views.dog_detail, name="get_dog_detail"),
    path('', views.home, name="home"),
    path('dogs/add/', views.form, name="add_dog"),
]
