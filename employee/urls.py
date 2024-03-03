from django.contrib.auth.views import LoginView
from django.urls import path

from . import views
from .views import UserRegisterView

app_name = "employee"

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("list/", views.IndexView.as_view(), name="index"),
    path("add/employee/", views.EmployeeAddView.as_view(), name="add_employee"),
    path(
        "update/employee/<str:eid>/",
        views.EmployeeUpdateView.as_view(),
        name="update_employee",
    ),
    path("employee/<str:eid>/", views.EmployeeDetailView.as_view(), name="detail"),
    path(
        "employee/<str:eid>/add/skill/",
        views.SkillAddView.as_view(),
        name="add_skill",
    ),
    path(
        "employee/skill/update/<int:pk>/",
        views.SkillUpdateView.as_view(),
        name="update_skill",
    ),
    path("delete/<str:eid>/", views.EmployeeDeleteView.as_view(), name="delete"),
]
