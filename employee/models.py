import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Employee(models.Model):
    eid = models.CharField("EID", max_length=50, primary_key=True)
    eno = models.CharField(
        "Employee No.", max_length=8, unique=True, default="00000000"
    )
    first_name = models.CharField(
        "First Name",
        max_length=20,
        default="XXXX",
    )
    middle_name = models.CharField("Middle Name", max_length=20, blank=True)
    last_name = models.CharField("Last Name", max_length=20, default="YYYY")
    full_name = models.CharField("Name", max_length=50)
    email = models.EmailField("e-mail", blank=True)
    dte = models.CharField("DTE", max_length=10, default="XXXX")
    office = models.CharField("Office", max_length=20, default="AIR")
    created_at = models.DateTimeField("Resister Date", auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.eid:
            base_eid = f"{self.first_name.lower()}.{self.last_name.lower()}"
            eid = base_eid
            counter = 0

            while Employee.objects.filter(eid=eid).exists():
                counter += 1
                eid = f"{base_eid}.{chr(64 + counter)}"  # A, B, C, ...

            self.eid = eid
            self.email = f"{self.eid}@accenture.com"
            self.full_name = f"{self.first_name} {self.middle_name} {self.last_name}"

        super(Employee, self).save(*args, **kwargs)

    def __str__(self):
        return "{0} {1} {2}".format(self.eid, self.full_name, self.dte)


class Project(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField("Project Name", max_length=50)
    start_date = models.DateTimeField("Start Date", default=timezone.now)
    end_date = models.DateTimeField("End Date", blank=True, null=True)
    description = models.TextField("Project Detail", blank=True)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name


class Skill(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=10)


class Training(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    completion_date = models.DateField()


class History(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    completion_date = models.DateField()
