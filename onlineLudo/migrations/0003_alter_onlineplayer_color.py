# Generated by Django 3.2.4 on 2021-07-06 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineLudo', '0002_auto_20210707_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlineplayer',
            name='color',
            field=models.CharField(default='', max_length=30),
        ),
    ]
