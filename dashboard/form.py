from secrets import choice
from urllib import request
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Review, Membership


class ReviewForms(ModelForm):
    name = forms.CharField(max_length=100, label=False,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    email = forms.EmailField(max_length=254, label=False,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    message = forms.CharField(label=False,
                              widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}))

    class Meta:
        model = Review
        fields = ['name', 'email', 'message']


class MembershipForm(ModelForm):
    
    name = forms.CharField(max_length=100, label=False, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'John Doe',
               'data-toggle': 'tooltip',
               'title': 'Nama Lengkap'}))

    birthplace = forms.CharField(max_length=100, label=False, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'New York',
               'data-toggle': 'tooltip',
               'title': 'Tempat Lahir'}))

    birthdate = forms.CharField(label=False, widget=forms.widgets.DateTimeInput(
        attrs={"type": "date",
               'class': 'form-control',
               'data-toggle': 'tooltip',
               'title': 'Tanggal Lahir'}))

    address = forms.CharField(max_length=254, label=False, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Greenwich Village',
               'data-toggle': 'tooltip',
               'title': 'Alamat Sekarang'}))

    email = forms.EmailField(max_length=254, label=False, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Johndoe@gmail.com',
               'pattern': '^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$'}))

    phone = forms.CharField(max_length=100, label=False, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': '087788998887',
               'pattern': '[0-9]\d{8,16}'}))

    PROGRAM_CHOICE = [
        ('the program', 'The Program'),
        ('gain weight', 'Gain weight'),
        ('lose weight', 'Lose weight'),
        ('other', 'Other')
    ]
    program = forms.CharField(max_length=100, label=False, widget=forms.Select(
        attrs={'class': 'form-control',
               'placeholder': 'The Program'}, 
        choices=PROGRAM_CHOICE))

    disability_disease = forms.CharField(max_length=250, label=False, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Do you have a disability?',
               'data-toggle': 'tooltip',
               'title': 'Ya / Tidak. \nJika memilih Ya, berikan penjelasan'}))

    gym_information = forms.CharField(max_length=250, label=False, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'How did you know Baginda Gym?',
               'data-toggle': 'tooltip',
               'title': 'Rekomendasi / Papan Iklan / Sosial Media / Lainnya. '
                        '\nJika Memilih Lainnya, Berikan Penjelasan'}))

    message = forms.CharField(label=False, widget=forms.Textarea(
        attrs={'class': 'form-control',
               'placeholder': 'Additional Message',
               'rows': '3'}))

    class Meta:
        model = Membership
        fields = ['name', 'birthplace', 'birthdate',
                  'address', 'email', 'phone', 'program',
                  'disability_disease', 'gym_information', 'message']


class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    username = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'johndoe'}))
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Johndoe@gmail.com',
               'pattern': '^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$'}))
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': '********',
                                                                  'pattern': '^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$'}))
    password2 = forms.CharField(label='Confirm Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': '********',
                                                                  'pattern': '^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
