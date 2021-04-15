# Generated by Django 3.2 on 2021-04-15 08:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 27, 8, 4, 43, 191858, tzinfo=utc), verbose_name='აქციის დასრულების თარიღი'),
        ),
    ]