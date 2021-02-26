from django.urls import include, path

from . import views

urlpatterns = [
    # path("users/", include("topit.urls")),
    path("rest-auth/", include("rest_auth.urls")),
    path("rest-auth/registration/", include("rest_auth.registration.urls")),
    path("", views.UserListView.as_view()),
    path("user/<int:pk>", views.UserUpdate.as_view()),
    path("user/<int:pk>/delete", views.UserDelete.as_view()),
    path("", include("djoser.urls")),
    path("", include("djoser.urls.authtoken")),
    path("list/", views.DataList.as_view(), name="data_list"),
    path("list/<int:pk>", views.DataDetail.as_view(), name="data_detail"),
    path("create/", views.DataCreate.as_view()),
    path("update/<int:pk>", views.DataUpdate.as_view()),
    path("delete/<int:pk>", views.DataDelete.as_view()),
]