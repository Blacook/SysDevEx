from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView

from .forms import EmployeeForm, SkillForm, TrainingForm
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
class IndexView(generic.ListView):
    model = Employee
    paginate_by = 10
    template_name = "employee_list.html"


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
    form_class = EmployeeForm
    template_name = "employee/employee_form.html"
    success_url = reverse_lazy("employee:index")


@method_decorator(login_required, name="dispatch")
class EmployeeUpdateView(generic.UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = "employee/employee_form.html"
    success_url = reverse_lazy("employee:index")

    def get_object(self, queryset=None):
        """URLからeidを取得し、それに基づいてEmployeeオブジェクトを返す"""
        eid = self.kwargs.get("eid")
        return get_object_or_404(Employee, eid=eid)

    def get_success_url(self):
        """更新が成功した後のリダイレクト先URLを指定"""
        employee = self.get_object()
        return reverse("employee:detail", kwargs={"eid": employee.eid})


@method_decorator(login_required, name="dispatch")
class EmployeeDeleteView(generic.DeleteView):
    model = Employee
    success_url = reverse_lazy("employee:index")


@method_decorator(login_required, name="dispatch")
class SkillAddView(generic.CreateView):
    model = Skill
    template_name = "employee/skill_form.html"
    form_class = SkillForm

    def get_initial(self):
        initial = super().get_initial()
        # URLからeidを取得し、対応するEmployeeオブジェクトを検索
        eid = self.kwargs.get("eid")
        employee = get_object_or_404(Employee, eid=eid)
        # EmployeeオブジェクトのIDをemployeeフィールドの初期値として設定
        initial["employee"] = employee.eid
        return initial

    def get_success_url(self):
        # 成功時には、追加されたSkillが紐づいているEmployeeの詳細ページに戻る
        eid = self.kwargs.get("eid")
        return reverse_lazy("employee:detail", kwargs={"eid": eid})


@method_decorator(login_required, name="dispatch")
class SkillUpdateView(UpdateView):
    model = Skill
    form_class = SkillForm
    template_name = "employee/skill_form.html"

    def get_success_url(self):
        # 成功時には、更新されたSkillが紐づいているEmployeeの詳細ページに戻る
        # この場合、Skillオブジェクトから関連するEmployeeのeidを取得しています
        skill = self.get_object()
        return reverse_lazy("employee:detail", kwargs={"eid": skill.employee.eid})


@method_decorator(login_required, name="dispatch")
class SkillDeleteView(generic.DeleteView):
    model = Skill
    form_class = SkillForm
    success_url = reverse_lazy("employee:index")
