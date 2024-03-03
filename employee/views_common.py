from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic


class BaseView(LoginRequiredMixin, generic.View):
    """すべてのビューで共通の設定を含むベースビュークラス"""

    pass


class EIDMixin:
    def get_object(self, queryset=None):
        """URLからeidを取得し、それに基づいてオブジェクトを返す"""
        eid = self.kwargs.get("eid")
        return get_object_or_404(self.model, eid=eid)


class SuccessUrlMixin:
    def get_success_url(self):
        """更新または追加が成功した後のリダイレクト先URLを指定"""
        return reverse_lazy("employee:detail", kwargs={"eid": self.object.employee.eid})
