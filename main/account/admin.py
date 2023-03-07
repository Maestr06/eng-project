from django.contrib import admin
from .models import Offer, Skill, Technology

# Register your models here.
admin.site.register(Technology)
admin.site.register(Skill)
admin.site.register(Offer)