# Generated by Django 5.0.4 on 2024-07-02 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits_tracker', '0005_alter_habit_periodic'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='date_last_send',
            field=models.DateField(blank=True, null=True, verbose_name='дата последней отправки'),
        ),
    ]