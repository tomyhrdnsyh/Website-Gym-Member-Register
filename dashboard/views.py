from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import ReviewForms, MembershipForm, CreateUserForm
from .models import Review, Instructor, Membership
from dateutil.relativedelta import relativedelta
from datetime import date
import random


IMG_REVIEWS = ['cardio-class.jpg', 'team-image01.jpg', 'team-image.jpg', 'crossfit-class.jpg', 'yoga-class.jpg']
IMG_INSTRUCTORS = ['gym-instructor-1.jpg', 'gym-instructor-2.jpg', 'gym-instructor-3.jpg', 'gym-instructor-4.jpeg']


def custom_template(params: dict, img: list, delay):
    for i, item in enumerate(params):
        item['name'] = ' '.join(item['name'].split()[:2])
        item['delay'] = delay + i * 100
        item['image'] = img[i] if i < len(img) else random.choice(img)

        if item.get('message'):
            if len(item['message']) > 50:
                item['message'] = item['message'][:50] + '...'
    return params


def dashboard(request, html=None):
    html = {'template': 'index.html'} if html is None else html

    # get data reviewers from database and view to template
    review = Review.objects.values()
    review = custom_template(review, IMG_REVIEWS, delay=400)

    # get data instructor from database and view to template
    instructor = Instructor.objects.values()
    instructor = custom_template(instructor, IMG_INSTRUCTORS, delay=700)

    # get data membership status from database and view to template
    membership_status = Membership.objects.all()

    # return to database if request is post
    if request.POST:
        # to_database adalah mengecek apakah POST dari form membership atau form reviews
        if 'membership' in request.POST: 
            to_database = MembershipForm(request.POST) 
            if to_database.is_valid():
                to_database.instance.user_account = request.user
                to_database.instance.start = date.today()
                to_database.instance.end = date.today() + relativedelta(months=+int(request.POST['member_class']))
                to_database.save()
        
        else:
            to_database = ReviewForms(request.POST)
            if to_database.is_valid():
                to_database.save()
        
        return redirect(request.POST.get('next', '/'))

    context = {'review': review, 'instructors': instructor,
               'review_form': ReviewForms, 'membership_status': membership_status,
               'membership_form': MembershipForm}

    return render(request, html['template'], context)


def dashboard_id(request):
    html = {'template': 'index_id.html'}
    return dashboard(request, html)


def login_page(request):
    form = UserCreationForm()

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage_id')
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {'login': form}
    return render(request, 'login.html', context)


def register_page(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + user)
            return redirect('/login')
        else:
            messages.warning(request, 'Register Failed!')
            return redirect('/register')

    context = {'register': form}
    return render(request, 'register.html', context)


def logout_user(request):
    logout(request)
    response = redirect('login')
    response.delete_cookie()
    return response
