# Generated by Django 4.1 on 2022-08-25 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_content', '0005_course_created_course_updated_lesson_created_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Kurs', 'verbose_name_plural': 'Kurslar'},
        ),
        migrations.AddField(
            model_name='course',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Yaradıldı'),
        ),
        migrations.AlterField(
            model_name='course',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Dəyişildi'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='course_content.course'),
        ),
    ]
