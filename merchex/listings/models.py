from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms

class Band(models.Model):
	def __str__(self):
		return f'{self.name}'
	
	class Genre(models.TextChoices):
		HIP_HOP = 'HH'
		SYNTH_POP = 'SP'
		ALTERNATIVE_ROCK = 'AR'

	genre = models.fields.CharField(choices=Genre.choices, max_length=5)
	name = models.fields.CharField(max_length=100)
	biography = models.fields.CharField(max_length=1000)
	year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900),MaxValueValidator(2021)])
	active = models.fields.BooleanField(default=True)
	official_homepage = models.fields.URLField(null=True, blank=True) 
	
    
class Listing(models.Model):
	def __str__(self):
		return f'{self.title}'
	class Types(models.TextChoices):
		Records='Records'
		Clothing='Clothing'
		Posters='Posters'
		Miscellaneous='Miscellaneous'

	title=models.fields.CharField(max_length=100)
	description=models.fields.CharField(max_length=1000)
	sold=models.fields.BooleanField(default=False)
	year=models.fields.IntegerField(validators=[MinValueValidator(1900),MaxValueValidator(2021)])
	types=models.fields.CharField(choices=Types.choices,max_length=20)
	band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
	
class BandForm(forms.Form):
   	name = forms.CharField(max_length=100)
   	biography = forms.CharField(max_length=1000)
   	year_formed = forms.IntegerField(min_value=1900, max_value=2021)
   	official_homepage = forms.URLField(required=False)
   	
class ListingForm(forms.Form):
	title=forms.fields.CharField(max_length=100)
	description=forms.fields.CharField(max_length=1000)
	year=forms.fields.IntegerField(validators=[MinValueValidator(1900),MaxValueValidator(2021)])


