from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    name = models.CharField(max_length=255, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' - ' + self.user.username

class Ingredient(models.Model):
    name = models.CharField(max_length=255, null=False)
    quantity = models.CharField(max_length=255, null=False)
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)
    product_id = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name + ' - ' + self.recipe.name
