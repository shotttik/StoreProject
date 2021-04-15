# Generated by Django 3.2 on 2021-04-15 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210415_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='end_date',
            field=models.DateField(auto_now_add=True, verbose_name='აქციის დასრულების თარიღი'),
        ),
    ]
