import re

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from .form import ReviewForms, MembershipForm, CreateUserForm
from django.contrib.auth.models import User
from .models import Review, Instructor, Membership, MembershipDetail, Payment, UserActivated
from dateutil.relativedelta import relativedelta
from datetime import date, datetime
import random
import smtplib
import midtransclient
import uuid


IMG_REVIEWS = ['cardio-class.jpg', 'team-image01.jpg', 'team-image.jpg', 'crossfit-class.jpg', 'yoga-class.jpg']
IMG_INSTRUCTORS = ['gym-instructor-1.jpg', 'gym-instructor-2.jpg', 'gym-instructor-3.jpg', 'gym-instructor-4.jpeg']
MY_EMAIL = 'bagindagym2022@gmail.com'
MY_PASSWORD = 'tpjctizchkgzeclk'


def custom_template(params: dict, img: list, delay):
    for i, item in enumerate(params):
        item['name'] = ' '.join(item['name'].split()[:2])
        item['delay'] = delay + i * 100
        item['image'] = img[i] if i < len(img) else random.choice(img)

        if item.get('message'):
            if len(item['message']) > 50:
                item['message'] = item['message'][:50] + '...'
    return params


def activate(request):
    context = {

    }
    if 'id' in request.GET:
        id_user = request.GET.get('id')
        user = User.objects.get(id=id_user)

        obj, status = UserActivated.objects.get_or_create(
            user=user,
            defaults={
                'user': user,
                'status': 'Activated'
            }
        )

    return render(request, 'activate.html', context)


def dashboard(request, html=None):
    html = {'template': 'index.html'} if html is None else html

    # check active status member
    status = Membership.objects.all()

    for item in status:
        # print(item.payment_status)
        if item.end < date.today() or str(item.payment_status) not in ["settlement", "capture"]:
            item.active_status = "Non Active"
            item.save()
        else:
            item.active_status = "Active"
            item.save()

    # get data reviewers from database and view to template
    review = Review.objects.values()
    review = custom_template(review, IMG_REVIEWS, delay=400)

    # get data instructor from database and view to template
    instructor = Instructor.objects.values('name', 'schedule')
    img_instructor = custom_template(instructor, IMG_INSTRUCTORS, delay=400)

    senin = [item['name'] for item in instructor if 'senin' in item['schedule']]
    selasa = [item['name'] for item in instructor if 'selasa' in item['schedule']]
    rabu = [item['name'] for item in instructor if 'rabu' in item['schedule']]
    kamis = [item['name'] for item in instructor if 'kamis' in item['schedule']]
    jumat = [item['name'] for item in instructor if 'jumat' in item['schedule']]
    # return to database if request is post
    if request.POST:
        # to_database adalah mengecek apakah POST dari form membership atau form reviews
        if 'membership' in request.POST:

            order_id = uuid.uuid1()
            membership = MembershipForm(request.POST)

            if membership.is_valid() and request.user.is_authenticated:
                save_membership_to_model(request, membership, unique_code=order_id)

                return call_payment(request, order_id)

            elif membership.is_valid() and not request.user.is_authenticated:
                customer_email = request.POST.get('email')
                username = request.POST.get('name').replace(' ', '').lower()
                password = 'rahasia2022'

                # save to user model
                user = User.objects.create_user(username=username, password=password,
                                                email=customer_email)
                save_membership_to_model(request, membership, user=user, unique_code=order_id)

                url = request.build_absolute_uri('/') + f'activate/?id={user.id}'
                send_email_password(customer_email, username, password, url)

                return call_payment(request, order_id)

        else:
            to_database = ReviewForms(request.POST)
            if to_database.is_valid():
                to_database.instance.name = request.user.username
                to_database.instance.email = request.user.email
                to_database.save()

        return redirect(request.POST.get('next', '/'))

    context = {'review': review, 'instructors': img_instructor,
               'review_form': ReviewForms,
               'membership_form': MembershipForm,
               'senin': senin,
               'selasa': selasa,
               'rabu': rabu,
               'kamis': kamis,
               'jumat': jumat,
               }

    # if user is login get data membership status from database and view to template
    if request.user.is_authenticated:

        # check status payment at Midtrans
        api_client = midtransclient.CoreApi(
            is_production=False,
            server_key='SB-Mid-server-01NTFWb6l738KBzH0OWZuhks',
            client_key='SB-Mid-client-UsEaLuaU7PMBbq_u'
        )

        membership_data = Membership.objects.filter(user_account=request.user)

        for item in membership_data:

            order = Payment.objects.get(id_payment=item.payment_status_id)
            if order.payment_status == 'process' or order.payment_status == 'pending':
                try:
                    status_response = api_client.transactions.status(item.payment_status_id)
                except Exception as e:
                    err = e
                    print('error', err)
                else:
                    order.payment_status = status_response.get('transaction_status')
                    order.payment_type = status_response.get('payment_type')
                    order.save()

        context['membership_status'] = membership_data

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


def send_email_password(customer_email, username, password, url):
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=str(customer_email),
                            msg='Subject:Username Password Baginda Gym\n\n'
                                'This is your username password \n\n'
                                f'Username : {username}\n'
                                f'Password : {password}\n'
                                f'link activated" {url}')


def save_payment_to_model(unique_code, price):
    payment = Payment(
        id_payment=unique_code,
        transaction_time=datetime.now(),
        gross_amount=price,
        payment_status='process'
    )
    payment.save()
    return payment


def save_membership_to_model(request, membership, unique_code, user=None):
    membership_detail = MembershipDetail.objects.get(id=request.POST.get('member_class'))
    payment_entity = save_payment_to_model(unique_code, membership_detail.price)

    member_month = ''.join(re.findall(r'\d', membership_detail.member_class))

    user = request.user if user is None else user
    membership.instance.user_account = user
    membership.instance.payment_status = payment_entity
    membership.instance.start = date.today()
    membership.instance.end = date.today() + relativedelta(months=+int(member_month))
    membership.save()


def payment_midtrans(request, price, order_id):
    snap = midtransclient.Snap(
        is_production=False,
        server_key='SB-Mid-server-01NTFWb6l738KBzH0OWZuhks',
        client_key='SB-Mid-client-UsEaLuaU7PMBbq_u'
    )

    param = {
        "transaction_details": {
            "order_id": f"{order_id}",
            "gross_amount": price
        }, "credit_card": {
            "secure": True
        },
        "callbacks": {
            "finish": request.build_absolute_uri('/')
        },
    }

    transaction = snap.create_transaction(param)
    return transaction


def call_payment(request, order_id):

    price = MembershipDetail.objects.get(id=request.POST.get('member_class')).price

    pay = payment_midtrans(request, price, order_id=order_id)
    return redirect(pay['redirect_url'])
