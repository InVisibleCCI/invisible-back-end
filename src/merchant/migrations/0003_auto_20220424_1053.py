# Generated by Django 3.2.11 on 2022-04-24 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_review'),
        ('merchant', '0002_navigationtracker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navigationtracker',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='navigations_trackers_event', to='event.event'),
        ),
        migrations.AlterField(
            model_name='navigationtracker',
            name='merchant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='navigation_trackers_merchant', to='merchant.merchant'),
        ),
    ]
