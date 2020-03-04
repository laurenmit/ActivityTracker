# Generated by Django 2.2.3 on 2019-07-31 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance_km', models.DecimalField(decimal_places=3, max_digits=8)),
                ('time_stamp', models.TimeField()),
                ('activity_type', models.CharField(max_length=15)),
                ('date', models.DateField()),
            ],
        ),
    ]
