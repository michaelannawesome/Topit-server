from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.UserListView.as_view()),
    path("", include("djoser.urls")),
    path("", include("djoser.urls.authtoken")),
]