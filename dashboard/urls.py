from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='homepage'),
    path('id/', views.dashboard_id, name='homepage_id'),
    path('login/', views.login_page, name='login'),
    path("logout/", LogoutView.as_view(template_name='login.html'), name="logout"),
    path('register/', views.register_page, name='register'),
]