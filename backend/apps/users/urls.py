from django.urls import path

from apps.users.views import CreateUserView, ListUsersView

urlpatterns = [
    path("", ListUsersView.as_view(), name="list_users_view"),
    path("/create_user", CreateUserView.as_view(), name="create_user_view")
]
