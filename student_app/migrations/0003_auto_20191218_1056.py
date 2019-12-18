# Generated by Django 2.2.7 on 2019-12-18 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0002_auto_20191218_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='college',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='college_student', to='student_app.College'),
        ),
    ]