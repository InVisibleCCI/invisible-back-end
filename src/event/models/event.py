from django.db import models

from common.models import Entity, Image
from event.models.category import Category, AccessibilityCategory


class Event(Entity):
    name = models.CharField(max_length=100, verbose_name="Nom de l'expérience")
    description = models.TextField(verbose_name="Description de l'expérience")
    categories = models.ManyToManyField(Category, related_name="event")
    accessibility_categories = models.ManyToManyField(AccessibilityCategory, related_name="event")
    images = models.ManyToManyField(Image, related_name="event")

    class Meta:
        app_label = "event"
        verbose_name = 'Expérience'
