# Generated by Django 2.1.5 on 2019-02-22 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_orders_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='name',
            field=models.CharField(max_length=111),
        ),
    ]