# Generated by Django 3.2.11 on 2022-04-24 10:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0004_event_is_exclusive'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(max_length=100, verbose_name="Titre de l'avis'")),
                ('description', models.TextField(verbose_name="Description de l'avis")),
                ('mark', models.FloatField(verbose_name="Note de l'avis'")),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reviews', to='event.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Avis',
            },
        ),
    ]
