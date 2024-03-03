from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = "employee"

urlpatterns = [
    path("list/", views.IndexView.as_view(), name="index"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("add/employee", views.EmployeeAddView.as_view(), name="add_employee"),
    path(
        "update/<str:eid>/", views.EmployeeUpdateView.as_view(), name="update_employee"
    ),
    path("delete/<str:eid>/", views.EmployeeDeleteView.as_view(), name="delete"),
    path("employee/<str:eid>/", views.EmployeeDetailView.as_view(), name="detail"),
]
