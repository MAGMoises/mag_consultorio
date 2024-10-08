from django.contrib import admin
from django.urls import path, include # adicionar include
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("accounts/", include("django.contrib.auth.urls")),
    path('contas/', include('contas.urls')), # url do app contas
    path('', include('pages.urls')), # url do app
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Adicionar Isto
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Adicionar Isto