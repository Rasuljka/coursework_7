# Generated by Django 5.0.4 on 2024-07-02 09:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits_tracker', '0003_alter_habit_periodic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='Время'),
        ),
    ]