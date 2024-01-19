# Generated by Django 4.2.9 on 2024-01-17 06:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mcqs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('question', models.CharField(max_length=1000)),
                ('option_A', models.CharField(max_length=100)),
                ('option_B', models.CharField(max_length=100)),
                ('option_C', models.CharField(max_length=100)),
                ('option_D', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('passw', models.CharField(max_length=50)),
                ('data_resgister', models.DateTimeField(default=datetime.datetime(2024, 1, 17, 12, 0, 19, 288006))),
            ],
        ),
    ]