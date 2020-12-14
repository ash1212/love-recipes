from django.conf import settings
from django.db import models
from django.urls import reverse


class Recipe(models.Model):
    MEASUREMENT_TYPES = [
        ('ml', 'ml'),
        ('l', 'l'),
        ('fl_oz', 'fl oz'),
        ('pt', 'pint'),

        ('tsp', 'tsp'),
        ('tbsp', 'tbsp'),
        ('oz', 'oz'),
        ('mg', 'mg'),
        ('g', 'g'),
        ('lb', 'lb'),
    ]
    COURSES = [
        ('starter', 'Starter'),
        ('main', 'Main'),
        ('dessert', 'Dessert'),
        ('side', 'Sides'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    ingredients = models.TextField(max_length=1000)
    measurement_type = models.CharField(choices=MEASUREMENT_TYPES, default='g', max_length=100)
    method = models.TextField(max_length=2000)
    course = models.CharField(choices=COURSES, max_length=50)
    time = models.CharField(max_length=50)
    servings = models.IntegerField()
    thumbnail = models.ImageField(upload_to='recipe_image/', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])


class RecipeYoutubeVideo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    url = models.URLField()


class RecipeExternalWebsite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    url = models.URLField()
    thumbnail = models.ImageField(upload_to='recipe_image/', blank=True)
