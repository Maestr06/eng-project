from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import UserLoginView

urlpatterns = [
    # login / logout urls with Django ootb views
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
]
