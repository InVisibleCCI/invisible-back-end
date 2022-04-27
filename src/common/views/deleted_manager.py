from django.db import models


class NotDeletedManager(models.Manager):
    def get_queryset(self):
        return super(NotDeletedManager, self).get_queryset().filter(deleted_at__isnull=True)
