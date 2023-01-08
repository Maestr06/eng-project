from django.contrib import admin
from .models import JobOffer, JobSkill, JobTechnology

# Register your models here.
admin.site.register(JobTechnology)
admin.site.register(JobSkill)
admin.site.register(JobOffer)