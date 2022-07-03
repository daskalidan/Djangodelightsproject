from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    quantity = models.FloatField(null=False, blank=False)
    unit = models.CharField(max_length=50, null=False, blank=False)
    unit_price = models.FloatField(null=False, blank=False)

class MenuItem(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(null=False, blank=False)

class Purchase(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)