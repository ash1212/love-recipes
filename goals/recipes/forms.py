from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from durationwidget.widgets import TimeDurationWidget

from .models import Recipe, RecipeYoutubeVideo, RecipeExternalWebsite

from django.contrib.auth import get_user_model
User = get_user_model()


class CreateRecipeForm(forms.ModelForm):
    time = forms.DurationField(widget=TimeDurationWidget(show_seconds=False, show_days=False), required=False)

    class Meta:
        model = Recipe
        fields = ['name', 'ingredients', 'method', 'course', 'time', 'servings', 'thumbnail']

    def convert_timedelta(self):
        days, seconds = Recipe.time.days, Recipe.time.seconds
        hours = days * 24 + seconds // 3600
        minutes = (seconds % 3600) // 60
        return hours, minutes


class CreateYoutubeRecipeForm(forms.ModelForm):
    class Meta:
        model = RecipeYoutubeVideo
        fields = [
            'name',
            'url',
        ]


class CreateRecipeExternalWebsiteForm(forms.ModelForm):
    class Meta:
        model = RecipeExternalWebsite
        fields = [
            'name',
            'url',
            'thumbnail',
        ]
