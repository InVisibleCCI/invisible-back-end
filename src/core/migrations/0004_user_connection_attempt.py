# Generated by Django 3.2.11 on 2022-04-21 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='connection_attempt',
            field=models.IntegerField(default=0, verbose_name='Essais de connexion'),
        ),
    ]
