from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views
from .views import UserRegisterView

app_name = "employee"

urlpatterns = [
    path("list/", views.IndexView.as_view(), name="index"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("add/employee/", views.EmployeeAddView.as_view(), name="add_employee"),
    path(
        "update/<str:eid>/", views.EmployeeUpdateView.as_view(), name="update_employee"
    ),
    path("delete/<str:eid>/", views.EmployeeDeleteView.as_view(), name="delete"),
    path("employee/<str:eid>/", views.EmployeeDetailView.as_view(), name="detail"),
]
