# Generated by Django 3.2.4 on 2021-07-09 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineLudo', '0008_alter_onlineplayer_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlineplayer',
            name='update',
            field=models.BooleanField(default=False),
        ),
    ]