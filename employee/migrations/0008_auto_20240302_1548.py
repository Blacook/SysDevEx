# Generated by Django 3.2 on 2024-03-02 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_auto_20240302_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='eid',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='EID'),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]