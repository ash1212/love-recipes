from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.views.generic import TemplateView, CreateView, ListView, DetailView

from .forms import CreateRecipeForm, CreateYoutubeRecipeForm, CreateRecipeExternalWebsiteForm
from .models import Recipe, RecipeYoutubeVideo, RecipeExternalWebsite

from django.contrib.auth import get_user_model
User = get_user_model()


class CreateRecipesView(TemplateView):
    template_name = 'recipe/create-recipe.html'

    def get(self, request, *args, **kwargs):
        form = CreateRecipeForm()
        posts = Recipe.objects.all().order_by('-created')

        args = {'form': form, 'posts': posts}
        return render(request, self.template_name, args)

    def post(self, request):
        form = CreateRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return HttpResponseRedirect('/my-recipes/')
        else:
            form = CreateRecipeForm()
        return render(request, "recipe/create-recipe.html", {"form": form})


class RecipeView(ListView):
    template_name = 'recipe/recipe-index.html'

    def get(self, request, *args, **kwargs):
        posts = Recipe.objects.filter(user=request.user).order_by('name')
        videos = RecipeYoutubeVideo.objects.filter(user=request.user)
        links = RecipeExternalWebsite.objects.filter(user=request.user)

        args = {
            'posts': posts,
            'videos': videos,
            'links': links,
        }
        return render(request, self.template_name, args)


def detail(request, pk):
    try:
        recipe = Recipe.objects.get(pk=pk)
    except Recipe.DoesNotExist:
        raise Http404("Recipe does not exist")
    return render(request, 'recipe/recipe-details.html', {'recipe': recipe})


class RecipeYoutubeVideoView(TemplateView):
    template_name = 'recipe/create-youtube-recipe.html'

    def get(self, request, *args, **kwargs):
        form = CreateYoutubeRecipeForm()

        args = {'form': form}
        return render(request, self.template_name, args)

    def post(self, request):
        form = CreateYoutubeRecipeForm(request.POST)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.save()
            return HttpResponseRedirect('/my-recipes/')
        else:
            form = CreateYoutubeRecipeForm()
        return render(request, "recipe/create-youtube-recipe.html", {"form": form})


class RecipeExternalWebsiteView(TemplateView):
    template_name = 'recipe/create-external-website-recipe.html'

    def get(self, request, *args, **kwargs):
        form = CreateRecipeExternalWebsiteForm()

        args = {'form': form}
        return render(request, self.template_name, args)

    def post(self, request):
        form = CreateRecipeExternalWebsiteForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.save()
            return HttpResponseRedirect('/my-recipes/')
        else:
            form = CreateRecipeExternalWebsiteForm()
        return render(request, "recipe/create-external-website-recipe.html", {"form": form})
