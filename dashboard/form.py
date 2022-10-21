from django.forms import ModelForm
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
               'placeholder': 'Johndoe@gmail.com'}))

    phone = forms.CharField(max_length=100, label=False, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': '123-456-7890',
               'pattern': '[0-9]{3}-[0-9]{3}-[0-9]+'}))

    program = forms.CharField(max_length=100, label=False, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'The program you choose',
               'data-toggle': 'tooltip',
               'title': 'Menaikan Berat Badan (Massa Otot) / Menurunkan Berat Badan / Lainnya.'
                              '\nJika Memilih Lainya, Berikan Penjelasan'}))

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
