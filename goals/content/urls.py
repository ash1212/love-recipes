from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import HomePageView

app_name = 'content'
urlpatterns = [
    path("", HomePageView.as_view(), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
