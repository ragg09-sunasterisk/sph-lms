# Generated by Django 4.1.7 on 2023-06-19 08:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_sph_lms', '0004_remove_course_company_course_trainee_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedLesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson', to='app_sph_lms.lesson')),
                ('trainee', models.ForeignKey(limit_choices_to={'is_trainer': False}, on_delete=django.db.models.deletion.CASCADE, related_name='trainee', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'CompletedLesson',
                'verbose_name_plural': 'CompletedLessons',
                'db_table': 'app_sph_lms_completed_lessons',
            },
        ),
    ]