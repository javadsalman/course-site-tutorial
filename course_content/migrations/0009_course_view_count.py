# Generated by Django 4.1 on 2022-09-16 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_content', '0008_lesson_title_az_lesson_title_ru'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]