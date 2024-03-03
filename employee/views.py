from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic.edit import CreateView

from .forms import EmployeeForm, SearchForm
from .models import Employee, Skill, Training


class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("employee:login")  # 登録後にログインページにリダイレクト

    def form_valid(self, form):
        valid = super().form_valid(form)
        # ここで追加の処理を行うことができます（例えばユーザーにメールを送信する等）
        return valid


@method_decorator(login_required, name="dispatch")
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


@method_decorator(login_required, name="dispatch")
class EmployeeAddView(generic.CreateView):
    model = Employee
    template_name = "employee/employee_form.html"
    form_class = EmployeeForm
    success_url = reverse_lazy("employee:index")


@method_decorator(login_required, name="dispatch")
class EmployeeUpdateView(generic.UpdateView):
    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy("employee:index")


@method_decorator(login_required, name="dispatch")
class EmployeeDeleteView(generic.DeleteView):
    model = Employee
    success_url = reverse_lazy("employee:index")


@method_decorator(login_required, name="dispatch")
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
