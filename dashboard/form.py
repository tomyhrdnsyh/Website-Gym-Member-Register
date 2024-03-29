from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Review, Membership, MembershipDetail


class ReviewForms(ModelForm):
    # name = forms.CharField(max_length=100, label=False,
    #                        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    # email = forms.EmailField(max_length=254, label=False,
    #                          widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    message = forms.CharField(label=False,
                              widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}))

    class Meta:
        model = Review
        fields = ['message']


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
        attrs={'placeholder': 'Birthdate',
               'type': 'date',
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

    member_class = forms.ModelChoiceField(
        queryset=MembershipDetail.objects.all(),
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    PROGRAM_CHOICE = [
        (None, 'The program you choose?'),
        ('Gain Weight', 'Gain Weight'),
        ('Lose Weight', 'Lose Weight'),
        ('Other', 'Other')
    ]
    program = forms.CharField(max_length=100, label=False, widget=forms.Select(
        attrs={'class': 'form-control', }, 
        choices=PROGRAM_CHOICE))

    DISABILITY_CHOICE = [
        (None, 'Do you have a disability?'),
        ('Yes', 'Yes'),
        ('No', 'No')
    ]
    disability_disease = forms.CharField(max_length=100, label=False, widget=forms.Select(
        attrs={'class': 'form-control', }, 
        choices=DISABILITY_CHOICE))

    GYM_INFORMATION_CHOICE = [
        (None, 'How did you know Baginda Gym?'),
        ('Recommendation', 'Recommendation'),
        ('Billboard', 'Billboard'),
        ('Social Media', 'Social Media'),
        ('Other', 'Other'),
    ]
    gym_information = forms.CharField(max_length=100, label=False, widget=forms.Select(
        attrs={'class': 'form-control', }, 
        choices=GYM_INFORMATION_CHOICE))

    message = forms.CharField(label=False, required=False, widget=forms.Textarea(
        attrs={'class': 'form-control',
               'placeholder': 'If you choose "Yes" on disability field or '
                              '"Other" in the other fields please explain here',
               'rows': '5'}))

    class Meta:
        model = Membership
        fields = ['name', 'birthplace', 'birthdate',
                  'address', 'email', 'phone', 'program',
                  'disability_disease', 'gym_information', 'member_class', 'message']


class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    pattern = '^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$'

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
                                                                  'pattern': pattern}))
    password2 = forms.CharField(label='Confirm Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': '********',
                                                                  'pattern': pattern}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
