# Generated by Django 3.2 on 2024-03-02 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0017_auto_20240302_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='End Date'),
        ),
    ]
