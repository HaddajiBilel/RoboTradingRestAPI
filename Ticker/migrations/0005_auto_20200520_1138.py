# Generated by Django 3.0.6 on 2020-05-20 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticker', '0004_auto_20200520_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticker',
            name='date',
            field=models.DateTimeField(),
        ),
    ]