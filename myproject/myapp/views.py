from django.shortcuts import render, get_object_or_404, redirect
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
    if request.method == "POST":
        name = request.POST.get("dog_name")
        race = request.POST.get("dog_race")
        age = request.POST.get("dog_age")
        image = request.FILES.get("image")

        Dog.objects.create(
            name=name,
            race=race,
            age=age,
            image=image
        )

        return redirect("home")
    
    return render(request, 'form.html')

def delete_dog(request, id):
    dog = get_object_or_404(Dog, id=id)

    if request.method == "POST":
        dog.delete()
    return redirect("get_all_dogs")

    # return render(request, "confirm_delete.html", {"dog": dog})

def alter_dog(request, id):
    dog = get_object_or_404(Dog, id=id)

    if request.method == "POST":
        dog.name = request.POST.get("dog_name")
        dog.race = request.POST.get("dog_race")
        dog.age = request.POST.get("dog_age")
        image = request.FILES.get("image")
        if image:
            dog.image = image
        dog.save()

        return redirect("home")
    return render(request, "form.html", {'dog': dog})