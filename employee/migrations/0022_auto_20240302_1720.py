# Generated by Django 3.2 on 2024-03-02 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0021_alter_employee_eid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='skill',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='training',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]