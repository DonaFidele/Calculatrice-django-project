from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


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
	hometown= models.fields.CharField(null=True,max_length=1000)
	
    
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
	
