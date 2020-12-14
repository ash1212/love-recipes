from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class HomePageView(TemplateView):

    template_name = "home.html"

    def myView(self, request):
        if request.user.is_authenticated():
            return redirect('/my-recipes/')
        else:
            return render(request, self.template_name)
