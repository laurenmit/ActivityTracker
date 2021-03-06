# Generated by Django 2.2.3 on 2019-08-04 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trackerapp', '0002_totals'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name_plural': 'Activities'},
        ),
        migrations.AlterModelOptions(
            name='totals',
            options={'verbose_name_plural': 'Totals'},
        ),
        migrations.AddField(
            model_name='totals',
            name='other_time',
            field=models.TimeField(default='00:00:00'),
        ),
        migrations.AddField(
            model_name='totals',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
