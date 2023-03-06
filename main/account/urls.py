from django.urls import path, include
from django.contrib.auth.decorators import login_required
from . import views
from .views import UserRegistrationView, OfferAddView, OfferDetailView, OfferListView


urlpatterns = [
    # login / logout urls with Django ootb views
    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('offer/<int:pk>/', login_required(OfferDetailView.as_view()), name='joboffer_detail'),
    path('offer/add/', login_required(OfferAddView.as_view()), name='addoffer'),
    path('offer/list/', OfferListView.as_view(), name='offerlist' )
]
