from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='homepage'),
    path('id/', views.dashboard_id, name='homepage'),
]