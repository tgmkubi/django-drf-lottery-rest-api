# Generated by Django 4.2.7 on 2023-11-10 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0005_lottery_winner'),
        ('competitor', '0003_competitor_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitor',
            name='lottery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competitors_of_lotteries', to='lottery.lottery'),
        ),
    ]
