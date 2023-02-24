from django.urls import path, include
from django.contrib.auth.decorators import login_required
from . import views
from .views import UserRegistrationView, OfferAddView, OfferDetailView

urlpatterns = [
    # login / logout urls with Django ootb views
    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('offer/int:id', login_required(OfferDetailView.as_view()), name='offerdetail'),
    path('offer/add/', login_required(OfferAddView.as_view()), name='addoffer'),
]
