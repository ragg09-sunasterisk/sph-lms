# Generated by Django 4.1.7 on 2023-05-31 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_sph_lms', '0003_alter_lesson_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='order',
            field=models.IntegerField(),
        ),
    ]