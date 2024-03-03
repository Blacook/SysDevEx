from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from .forms import EmployeeUpdateForm, SearchForm
from .models import Employee, Skill, Training


class UserLoginView(LoginView):
    template_name = "employee/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("employee:list")  # ログイン後にリダイレクトするURL


class EmployeeDetailView(generic.DetailView):
    model = Employee
    template_name = "employee/employee_detail.html"

    def get_object(self):
        # Use 'eid' from the URL kwargs to fetch the Employee instance
        eid = self.kwargs.get("eid")
        return get_object_or_404(Employee, eid=eid)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employee = self.get_object()
        context["skills"] = Skill.objects.filter(employee=employee)
        context["trainings"] = Training.objects.filter(employee=employee)
        return context


class EmployeeAddView(generic.CreateView):
    model = Employee
    form_class = EmployeeUpdateForm
    success_url = reverse_lazy("employee:index")


class EmployeeUpdateView(generic.UpdateView):
    model = Employee
    form_class = EmployeeUpdateForm
    success_url = reverse_lazy("employee:index")


class EmployeeDeleteView(generic.DeleteView):
    model = Employee
    success_url = reverse_lazy("employee:index")


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
