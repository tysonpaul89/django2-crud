# Generated by Django 2.1.1 on 2018-09-24 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20180924_0430'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
    ]
