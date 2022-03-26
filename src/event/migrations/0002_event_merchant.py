# Generated by Django 3.2.11 on 2022-03-25 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('merchant', '0001_initial'),
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='merchant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='merchant.merchant'),
        ),
    ]
