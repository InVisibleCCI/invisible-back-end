import uuid

from django.db import models
from django.utils import timezone
from datetime import datetime

class Entity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(
        blank=True,
        auto_now=True
    )
    deleted_at = models.DateTimeField(null=True, blank=True)

    def mark_as_deleted(self, date: datetime = None, save: bool = False):
        if self.deleted:
            return

        self.deleted = date or timezone.now()

        if save:
            self.save()

    def delete(self, using=None, keep_parents=False):
        self.mark_as_deleted(save=True)

    class Meta:
        abstract = True
