# Generated by Django 3.0.6 on 2020-05-21 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ticker', '0003_auto_20200521_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicator',
            name='ticker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='indicators', serialize=False, to='Ticker.Ticker'),
        ),
    ]