from django.urls import path

from .apis import dummy


app_name = "frontend"
urlpatterns = [
	path("dummy/", dummy, name="dummy"),
]
