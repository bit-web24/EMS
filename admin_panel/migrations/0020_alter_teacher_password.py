# Generated by Django 5.0.6 on 2024-06-27 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0019_remove_teacher_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='password',
            field=models.CharField(default='teacher', max_length=100),
        ),
    ]
