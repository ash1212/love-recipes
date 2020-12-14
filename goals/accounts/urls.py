from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView

from .views import registerView, loginView, logoutView

app_name = 'accounts'
urlpatterns = [
    path("register/", registerView, name='register'),
    path("login/", loginView, name='login'),
    path("logout/", logoutView, name='logout'),
    path("thanks/", TemplateView.as_view(template_name="accounts/thanks.html"), name='thanks'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
