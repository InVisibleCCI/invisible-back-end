# Generated by Django 3.2.11 on 2022-03-21 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchant',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description du commerçant'),
        ),
    ]
