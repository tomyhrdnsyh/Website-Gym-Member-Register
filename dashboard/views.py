from django.shortcuts import render, redirect
from .form import ReviewForms, MembershipForm
from .models import Review
from datetime import datetime
import random


def dashboard(request):
    # get data from database and view to template
    review = Review.objects.values()
    review = custom(review)
    
    # return to database if request is post
    if request.POST:
        # to_database adalah mengecek apakah POST dari form membership atau form reviews
        to_database = MembershipForm(request.POST) if 'membership' in request.POST else ReviewForms(request.POST)

        if to_database.is_valid():
            to_database.save()

        return redirect('/')

    return render(request, 'index.html', {'review': review, 'review_form': ReviewForms, 'membership_form': MembershipForm})


def custom(review: dict):
    img = ['cardio-class.jpg', 'crossfit-class.jpg', 'yoga-class.jpg']
    for i, item in enumerate(review):
        item['delay'] = 400 + i * 100
        item['image'] = img[i] if i < len(img) else random.choice(img)
    return review