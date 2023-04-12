from django.urls import path
from . import views
from account.views import UserListView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('', views.login_user, name="login"),
    path('users-index', UserListView.as_view(), name="users-index"),
    path('register-user', views.register_user, name="register-user"),
    path('update-user/<int:pk>/', UserUpdateView.as_view(), name="update-user"),
    path('delete-user/<int:pk>/', UserDeleteView.as_view(), name="delete-user"),
]
