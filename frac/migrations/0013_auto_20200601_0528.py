# Generated by Django 3.0.6 on 2020-06-01 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frac', '0012_auto_20200601_0525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='available',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
