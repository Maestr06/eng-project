from django.db import models

# Create your models here.



class JobListing(models.Model):
    listing_title = models.CharField(max_length=100, default='Oferta pracy')
    listing_description = models.CharField(max_length=250, default='Opis oferty pracy')
