# Generated by Django 3.0.7 on 2021-05-01 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20210501_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_info1',
            name='product_contact',
            field=models.IntegerField(default=20),
        ),
    ]
