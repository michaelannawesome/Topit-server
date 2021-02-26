from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.UserListView.as_view()),
    path("", include("djoser.urls")),
    path("", include("djoser.urls.authtoken")),
    path("list/", views.DataList.as_view(), name="data_list"),
    path("list/<int:pk>", views.DataDetail.as_view(), name="data_detail"),
    path("create/", views.DataCreate.as_view()),
]