import uuid

from django.db import models

class Entity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(
        blank=True,
        auto_now=True
    )
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        abstract = True