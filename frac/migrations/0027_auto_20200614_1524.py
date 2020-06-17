# Generated by Django 3.0.6 on 2020-06-14 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frac', '0026_auto_20200612_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sandtype',
            name='date_prefill',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='sandtype',
            name='loading_facility',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='frac.LoadingFacility'),
        ),
        migrations.AlterField(
            model_name='sandtype',
            name='po',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='sandtype',
            name='total_sand',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
