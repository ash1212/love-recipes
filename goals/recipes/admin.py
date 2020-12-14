from django.contrib import admin

from .models import Recipe, RecipeYoutubeVideo, RecipeExternalWebsite


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):

    list_display = ('name', 'course', 'time', 'servings')
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ()


@admin.register(RecipeYoutubeVideo)
class YouTubeRecipesAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ()


@admin.register(RecipeExternalWebsite)
class RecipeExternalWebsiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ()
