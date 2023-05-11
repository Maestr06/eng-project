import django_filters
from django_filters import filters
from .models import Offer, Technology, Skill, Seniority, Location
from django.db import models
from django import forms

class PostFilter(django_filters.FilterSet):
    # offer_tech = filters.ModelChoiceFilter(queryset=Technology.objects.all())
    offer_skills = filters.ModelMultipleChoiceFilter(queryset=Skill.objects.all(), widget=forms.CheckboxSelectMultiple)
    # offer_seniority = filters.ModelChoiceFilter(queryset=Seniority.objects.all())
    # offer_location = filters.ModelChoiceFilter(queryset=Location.objects.all())
    
    class Meta:
        model = Offer
        fields = ['offer_tech', 'offer_skills', 'offer_seniority', 'offer_location']

        # filter_overrides = {
        #     models.ManyToManyField: {
        #         'filter_class': filters.ModelMultipleChoiceFilter(widget = forms.CheckboxSelectMultiple),
        #         'extra': {
        #             'widget': forms.CheckboxSelectMultiple,
        #         },
        #     },
        # }