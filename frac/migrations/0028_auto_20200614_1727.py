# Generated by Django 3.0.6 on 2020-06-14 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frac', '0027_auto_20200614_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sandtype',
            name='loading_facility',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='frac.LoadingFacility'),
        ),
    ]
