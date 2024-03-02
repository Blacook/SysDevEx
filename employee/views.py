from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .forms import SearchForm
from .models import Employee


class UserLoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("list")  # ログイン後にリダイレクトするURL


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = "employee_detail.html"

    def get_object(self):
        eid = self.kwargs.get("eid")
        return Employee.objects.get(eid=eid)


class IndexView(generic.ListView):
    model = Employee
    paginate_by = 10
    template_name = "employee_list.html"

    def get_context_data(self):
        """テンプレートへ渡す辞書の作成"""
        context = super().get_context_data()
        context["form"] = SearchForm(self.request.GET)  # 基の辞書に、formを追加
        return context

    def get_queryset(self):
        """テンプレートへ渡す「employee_list」を作成する"""
        form = SearchForm(self.request.GET)
        form.is_valid()  # これをしないと、cleaned_dataができない!!!

        # まず、全社員を取得
        queryset = super().get_queryset()

        # 部署の選択があれば、部署で絞り込み(filter)
        department = form.cleaned_data["department"]
        if department:
            queryset = queryset.filter(department=department)

        return queryset
