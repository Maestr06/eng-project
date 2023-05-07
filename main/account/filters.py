import django_filters
from .models import Offer

class PostFilter(django_filters.FilterSet):

    class Meta:
        model = Offer
        fields = ['offer_tech', 'offer_skills', 'offer_seniority', 'offer_location']