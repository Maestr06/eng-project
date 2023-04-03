from django.urls import path, include
from django.contrib.auth.decorators import login_required
from . import views
from .views import UserRegistrationView, OfferAddView, OfferDetailView, OfferListView, UserEditView#, CompanyEditView


urlpatterns = [
    # login / logout urls with Django ootb views
    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('offer/<int:pk>/', login_required(OfferDetailView.as_view()), name='offer_detail'),
    path('offer/add/', login_required(OfferAddView.as_view()), name='offer_add'),
    path('offer/list/', OfferListView.as_view(), name='offer_list' ),
    path('edit/user/', UserEditView.as_view(), name='edit_user')
]
