from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views
from .views import EmployeeDetailView, UserLoginView

app_name = "employee"

urlpatterns = [
    path("list/", views.IndexView.as_view(), name="index"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("employee/<str:eid>/", EmployeeDetailView.as_view(), name="detail"),
]
