# Generated by Django 4.2.7 on 2023-11-12 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0005_lottery_winner'),
    ]

    operations = [
        migrations.AddField(
            model_name='lottery',
            name='select_winner',
            field=models.BooleanField(default=False),
        ),
    ]