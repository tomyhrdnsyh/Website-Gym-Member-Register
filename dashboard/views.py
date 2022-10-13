from django.shortcuts import render, redirect
from .models import Review
import random

# Create your views here.
def dashboard(request):
    review = Review.objects.values()
    review = custom(review)

    return render(request, 'index.html', {'review': review})

def custom(review: dict):
    img = ['cardio-class.jpg', 'crossfit-class.jpg', 'yoga-class.jpg']
    for i, item in enumerate(review):
        item['delay'] = 400 + i * 100
        item['image'] = img[i] if len(img) >= i else random.choice(img)
    return review