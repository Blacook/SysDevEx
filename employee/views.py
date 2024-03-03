from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView

from .forms import EmployeeForm, SkillForm
from .models import Employee, Skill, Training
from .views_common import BaseView, EIDMixin, SuccessUrlMixin


class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("employee:login")  # 登録後にログインページにリダイレクト

    def form_valid(self, form):
        valid = super().form_valid(form)
        # ここで追加の処理を行うことができます（例えばユーザーにメールを送信する等）
        return valid


class IndexView(BaseView, generic.ListView):
    model = Employee
    paginate_by = 5
    template_name = "employee_list.html"


class EmployeeDetailView(BaseView, EIDMixin, generic.DetailView):
    model = Employee
    template_name = "employee/employee_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employee = self.get_object()
        context["skills"] = Skill.objects.filter(employee=employee)
        context["trainings"] = Training.objects.filter(employee=employee)
        return context


class EmployeeAddView(BaseView, generic.CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = "employee/employee_form.html"
    success_url = reverse_lazy("employee:index")


class EmployeeUpdateView(BaseView, EIDMixin, generic.UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = "employee/employee_form.html"

    def get_success_url(self):
        """更新が成功した後のリダイレクト先URLを指定"""
        return reverse_lazy("employee:detail", kwargs={"eid": self.get_object().eid})


class EmployeeDeleteView(BaseView, generic.DeleteView):
    model = Employee
    success_url = reverse_lazy("employee:index")


class SkillAddView(BaseView, generic.CreateView):
    model = Skill
    form_class = SkillForm
    template_name = "employee/skill_form.html"

    def get_initial(self):
        initial = super().get_initial()
        # URLからeidを取得し、対応するEmployeeオブジェクトを検索
        eid = self.kwargs.get("eid")
        # EmployeeオブジェクトのIDをemployeeフィールドの初期値として設定
        initial["employee"] = eid
        return initial

    def get_success_url(self):
        eid = self.kwargs.get("eid")
        return reverse_lazy("employee:detail", kwargs={"eid": eid})


class SkillUpdateView(BaseView, SuccessUrlMixin, UpdateView):
    model = Skill
    form_class = SkillForm
    template_name = "employee/skill_form.html"


class SkillDeleteView(BaseView, SuccessUrlMixin, generic.DeleteView):
    model = Skill
    form_class = SkillForm
