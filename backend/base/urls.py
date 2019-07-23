from django.conf import settings
from django.contrib import admin
from django.urls import include, path

admin.site.index_title = "Admin Index Title"
admin.site.site_header = "Admin Site Header"
admin.site.site_title = "Admin Site Title"

urlpatterns = [
	path("admin/", admin.site.urls),
	path("api/v1/frontend/", include("frontend.api_urls", namespace="frontend-api")),
	path("", include("frontend.urls", namespace="frontend-view")),
]

if settings.DEBUG:
	from django.conf.urls.static import static
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
