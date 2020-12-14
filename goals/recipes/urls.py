from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import CreateRecipesView, RecipeView, RecipeYoutubeVideoView, RecipeExternalWebsiteView, detail

app_name = 'recipes'
urlpatterns = [
    path("", RecipeView.as_view(), name='my-recipes'),
    path("create/", CreateRecipesView.as_view(), name='create'),
    path("new-video/", RecipeYoutubeVideoView.as_view(), name='new-video'),
    path("new-website/", RecipeExternalWebsiteView.as_view(), name='new-website'),
    path('detail/<int:pk>/', detail, name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
