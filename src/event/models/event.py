from django.db import models
from django.db.models import Manager, Avg, Count, FloatField
from django.db.models.functions import Coalesce

from common.models import Entity
from common.views.deleted_manager import NotDeletedManager
from event.models.category import Category, AccessibilityCategory

"""
Calculate in DB the average mark of reviews and their count 
"""


class EventManager(models.Manager):
    def get_queryset(self):
        return Event.not_deleted_objects.get_queryset().annotate(
            average_mark=Coalesce(Avg('reviews__mark'), 0, output_field=FloatField()),
            reviews_count=Count('reviews'),
        )


class Event(Entity):
    class EventDifficultyChoices(models.IntegerChoices):
        easy = 1, 'Facile'
        medium = 2, 'Moyenne'
        hard = 3, "Difficile"

    name = models.CharField(max_length=100, verbose_name="Nom de l'expérience")
    description = models.TextField(verbose_name="Description de l'expérience")
    categories = models.ManyToManyField(Category, related_name="event", verbose_name="Catégorie")
    accessibility_categories = models.ManyToManyField(AccessibilityCategory,
                                                      related_name="event",
                                                      verbose_name="Catégorie d'accessibilité")
    images = models.ManyToManyField("common.Image", related_name="event")
    address = models.ForeignKey('common.Address', on_delete=models.CASCADE, verbose_name="Adresse de l'événement")
    difficulty = models.IntegerField(choices=EventDifficultyChoices.choices,
                                     null=True,
                                     blank=True,
                                     verbose_name='Difficulté')
    merchant = models.ForeignKey('merchant.Merchant', on_delete=models.PROTECT, null=True)
    is_exclusive = models.BooleanField(verbose_name="Expérience exclusive", default=False)

    class CardColorChoices(models.TextChoices):
        pink = '#FF7E7E', "Rose"
        flirt = '#A02074', "Flirt"
        magenta = '#CF0063', "Magenta"
        blue = '#2F789D', "Blue"
        lightBlue = '#06C7F2', "Bleu clair"
        darkBlue = '#5B53AE', "Bleu foncé"
        purple = '#7F20A0', "Violet"
        green = '#20A091', "Vert"
        orange = '#EF9935', "Orange"

    card_color = models.TextField(choices=CardColorChoices.choices, default=CardColorChoices.pink)

    objects = Manager()
    objects_with_mark = EventManager()
    not_deleted_objects = NotDeletedManager()

    class Meta:
        app_label = "event"
        verbose_name = 'Expérience'

    def __str__(self):
        return self.name

    @property
    def short_description(self):
        return "..."
