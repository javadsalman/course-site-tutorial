# Generated by Django 4.1 on 2022-08-25 16:58

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_content', '0006_alter_course_options_course_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_content.course'),
        ),
    ]