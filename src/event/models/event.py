from django.db import models

from common.models import Entity, Image
from event.models.category import Category, AccessibilityCategory


class Event(Entity):
    class EventDifficultyChoices(models.IntegerChoices):
        easy = 1, 'Facile'
        medium = 2, 'Moyenne'
        hard = 3, "Difficile"

    name = models.CharField(max_length=100, verbose_name="Nom de l'expérience")
    description = models.TextField(verbose_name=" Courte description de l'expérience")
    categories = models.ManyToManyField(Category, related_name="event")
    accessibility_categories = models.ManyToManyField(AccessibilityCategory, related_name="event")
    images = models.ManyToManyField(Image, related_name="event")
    address = models.ForeignKey('common.Address', on_delete=models.CASCADE)
    difficulty = models.IntegerField(choices=EventDifficultyChoices.choices, null=True, blank=True)
    merchant = models.ForeignKey('merchant.Merchant', on_delete=models.PROTECT, null=True)

    class Meta:
        app_label = "event"
        verbose_name = 'Expérience'

    @property
    def short_description(self):
        return "..."
