# Generated by Django 3.2 on 2021-04-15 14:32

import datetime
from django.db import migrations, models
import django_editorjs_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='conditions',
            field=django_editorjs_fields.fields.EditorJsTextField(blank=True, verbose_name='აქციის პირობები'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=django_editorjs_fields.fields.EditorJsTextField(blank=True, verbose_name='აღწერა'),
        ),
        migrations.AlterField(
            model_name='product',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 27, 14, 32, 2, 202080), verbose_name='აქციის დასრულების თარიღი'),
        ),
    ]
