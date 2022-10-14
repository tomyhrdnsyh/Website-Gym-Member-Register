from django.forms import ModelForm
from django import forms
from .models import Review, Membership

class ReviewForms(ModelForm):
    name = forms.CharField(max_length=100, label=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    email = forms.EmailField(max_length=254, label=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    message = forms.CharField(label=False, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}))
    
    class Meta:
        model = Review
        fields = ['name', 'email', 'message']

class MembershipForm(ModelForm):
    name = forms.CharField(max_length=100, label=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'John Doe'}))
    email = forms.EmailField(max_length=254, label=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Johndoe@gmail.com'}))
    phone = forms.CharField(max_length=100, label=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '123-456-7890', 'pattern': '[0-9]{3}-[0-9]{3}-[0-9]+'}))
    message = forms.CharField(label=False, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Additional Message', 'rows': '3'}))
    
    class Meta:
        model = Membership
        fields = ['name', 'email', 'phone', 'message']