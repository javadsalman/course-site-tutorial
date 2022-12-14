# Generated by Django 4.1 on 2022-08-23 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_student_user_alter_teacher_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='biography',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='teacher_photos/'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='website',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
    ]
