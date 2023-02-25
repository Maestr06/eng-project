from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic.detail import DetailView
from .models import JobOffer, JobSkill, JobTechnology
from .forms import OfferForm, UserRegistrationForm

@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})

class UserRegistrationView(View):

    def get(self, request):
        user_form = UserRegistrationForm()
        return render(request, 'account/register.html', {'user_form': user_form})
    
    def post(self, request):
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
        else:
            return render(request, 'account/register.html', {'user_form': user_form})


class OfferAddView(View):

    def get(self, request):
        offer_form = OfferForm()
        return render(request, 'account/offer_add.html', {'form': offer_form})

    def post(self, request):
        offer_form = OfferForm(request.POST)
        if offer_form.is_valid():
            new_offer = offer_form.save(commit=False)
            new_offer.save()
            return render(request, 'account/dashboard.html', {'new_offer': new_offer})
            
class OfferDetailView(DetailView):

    model = JobOffer

    # def get(self, request, offer_id):
    #     try:
    #         offer = JobOffer.objects.get(pk=offer_id)
    #     except JobOffer.DoesNotExist:
    #         raise Http404("Offer with this id does not exist")
    #     return render(request, 'account/offer_detail.html', {'offer': offer})