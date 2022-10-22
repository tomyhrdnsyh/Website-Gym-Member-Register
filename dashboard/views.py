from django.shortcuts import render, redirect
from .form import ReviewForms, MembershipForm
from .models import Review, Instructor
import random

IMG_REVIEWS = ['cardio-class.jpg', 'team-image01.jpg', 'team-image.jpg', 'crossfit-class.jpg', 'yoga-class.jpg']
IMG_INSTRUCTORS = ['gym-instructor-1.jpg','gym-instructor-2.jpg', 'gym-instructor-3.jpg', 'gym-instructor-4.jpeg']


def dashboard(request):
    # get data reviewers from database and view to template
    review = Review.objects.values()
    review = custom_template(review, IMG_REVIEWS, delay=400)

    # get data instructor from database and view to template
    instructor = Instructor.objects.values()
    instructor = custom_template(instructor, IMG_INSTRUCTORS, delay=700)

    # return to database if request is post
    if request.POST:
        # to_database adalah mengecek apakah POST dari form membership atau form reviews
        to_database = MembershipForm(request.POST) if 'membership' in request.POST else ReviewForms(request.POST)

        if to_database.is_valid():
            to_database.save()

        return redirect('/')

    return render(request, 'index.html', {'review': review, 'instructors': instructor, 'review_form': ReviewForms,
                                          'membership_form': MembershipForm})


def custom_template(params: dict, img: list, delay):
    for i, item in enumerate(params):
        item['name'] = ' '.join(item['name'].split()[:2])
        item['delay'] = delay + i * 100
        item['image'] = img[i] if i < len(img) else random.choice(img)

        if item.get('message'):
            if len(item['message']) > 50:
                item['message'] = item['message'][:50] + '...'
    return params


