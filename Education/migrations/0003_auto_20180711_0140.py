# Generated by Django 2.0.2 on 2018-07-10 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Education', '0002_auto_20180710_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='percentage',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
