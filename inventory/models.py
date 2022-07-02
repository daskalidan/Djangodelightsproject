from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    quantity = models.FloatField(null=False, blank=False)
    unit = models.CharField(max_length=50, null=False, blank=False)
    unit_price = models.FloatField(null=False, blank=False)

class MenuItem(models.Model):
    pass

class RecipeRequirement(models.Model):
    pass

class Purchase(models.Model):
    pass