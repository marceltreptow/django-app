from django.shortcuts import render, get_object_or_404
from .models import Dog

# Create your views here.

def get_all_dogs(request):
    dogs = Dog.objects.all()
    for dog in dogs:
        print(dog)
    return render(request, 'index.html', {'dogs': dogs})

def dog_detail(request, id):
    dog = get_object_or_404(Dog, id=id)
    return render(request, 'detail.html', {'dog': dog})

def home(request):
    return render(request, 'homepage.html')

def form(request):
    return render(request, 'form.html')