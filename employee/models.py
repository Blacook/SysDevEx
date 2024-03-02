from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class DTE(models.Model):
    name = models.CharField("DTE", max_length=20)
    created_at = models.DateTimeField("日付", default=timezone.now)

    def __str__(self):
        return self.name


class Employee(models.Model):
    eid = models.CharField("EID", max_length=10, primary_key=True)
    eno = models.CharField("社員番号", max_length=10)
    first_name = models.CharField(
        "名",
        max_length=20,
    )
    middle_name = models.CharField("ミドル", max_length=20, blank=True)
    last_name = models.CharField("姓", max_length=20)
    full_name = models.CharField(
        "氏名", max_length=50, default=f"{first_name} {middle_name} {last_name}"
    )
    email = models.EmailField("e-mail", blank=True, default=f"{eid}@accenture.com")
    dte = models.ForeignKey(
        DTE,
        verbose_name="DTE",
        on_delete=models.PROTECT,
    )
    office = models.CharField("オフィス", max_length=20, blank=True)
    created_at = models.DateTimeField("登録日", default=timezone.now)

    def __str__(self):
        return "{0} {1} {2}".format(self.last_name, self.first_name, self.dte)


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("プロジェクト名", max_length=50)

    start_date = models.DateTimeField("開始日", default=timezone.now)
    end_date = models.DateTimeField("終了日", blank=True, null=True)
    description = models.TextField("プロジェクトの詳細", blank=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=10)


class Training(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    completion_date = models.DateField()


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    completion_date = models.DateField()
