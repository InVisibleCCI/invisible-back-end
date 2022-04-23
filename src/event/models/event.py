from django.db import models
from django.db.models import Manager

from common.models import Entity
from common.views.deleted_manager import NotDeletedManager
from event.models.category import Category, AccessibilityCategory


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
    is_exclusive = models.BooleanField(verbose_name="Expérience exclusive",default=False)

    objects = Manager()
    not_deleted_objects = NotDeletedManager()

    class Meta:
        app_label = "event"
        verbose_name = 'Expérience'

    def __str__(self):
        return self.name


    @property
    def short_description(self):
        return "..."
