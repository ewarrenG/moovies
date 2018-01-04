from django.conf.urls import url
from django.contrib import admin

# Use include() to add URLS from the catalog application and authentication system
from django.conf.urls import include

urlpatterns = [
    url(r'admin/', admin.site.urls),
]
urlpatterns += [
    url(r'^blog/', include('blog.urls')),
]


# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

#urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
urlpatterns += [
    url(r'^$', RedirectView.as_view(url='/blog/', permanent=True)), #crucial
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
	url(r'^accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
	urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

