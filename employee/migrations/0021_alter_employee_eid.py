# Generated by Django 3.2 on 2024-03-02 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0020_alter_employee_eid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='eid',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='EID'),
        ),
    ]