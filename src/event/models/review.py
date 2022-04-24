from django.db import models
from django.db.models import Manager

from common.models import Entity
from common.views.deleted_manager import NotDeletedManager
from event.models import Event
from core.models import User

class Review(Entity):
    title = models.CharField(max_length=100, verbose_name="Titre de l'avis'")
    description = models.TextField(verbose_name="Description de l'avis")
    mark = models.FloatField(verbose_name="Note de l'avis'")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    event = models.ForeignKey(Event, on_delete=models.PROTECT, related_name="reviews")

    objects = Manager()
    not_deleted_objects = NotDeletedManager()

    class Meta:
        app_label = "event"
        verbose_name = 'Avis'

    def __str__(self):
        return self.title
