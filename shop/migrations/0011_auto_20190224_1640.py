# Generated by Django 2.1.5 on 2019-02-24 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20190224_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='qty',
            field=models.IntegerField(default=0, max_length=1000),
        ),
    ]