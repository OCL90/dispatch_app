# Generated by Django 3.0.6 on 2020-06-03 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frac', '0013_auto_20200601_0528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appt_time', models.CharField(max_length=50, null=True)),
                ('load_weight', models.CharField(max_length=50, null=True)),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='frac.Driver')),
                ('sand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='frac.SandType')),
                ('well_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='frac.Well')),
            ],
        ),
    ]
