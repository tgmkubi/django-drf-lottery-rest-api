# Generated by Django 4.2.7 on 2023-11-06 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lottery',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='lottery',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]