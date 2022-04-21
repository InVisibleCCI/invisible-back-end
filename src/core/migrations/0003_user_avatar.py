# Generated by Django 3.2.11 on 2022-03-29 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_address_user'),
        ('core', '0002_user_is_merchant'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='common.image'),
        ),
    ]
