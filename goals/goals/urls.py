from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('', include("content.urls")),
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),
    path('my-recipes/', include("recipes.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
