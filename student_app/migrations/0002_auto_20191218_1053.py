# Generated by Django 2.2.7 on 2019-12-18 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(auto_now=True),
        ),
    ]
