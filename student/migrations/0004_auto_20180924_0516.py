# Generated by Django 2.1.1 on 2018-09-24 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_customuser_isactive'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='isActive',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
