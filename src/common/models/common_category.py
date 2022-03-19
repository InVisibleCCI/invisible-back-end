from django.db import models

from common.models.entity import Entity


class CommonCategory(Entity):
    name = models.CharField(max_length=20, verbose_name="Nom de la catégorie")

    class Meta:
        abstract = True
