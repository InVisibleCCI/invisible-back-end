from django.db import models

from common.models import Entity
from core.models import User


class Address(Entity):
    line1 = models.CharField(max_length=150, verbose_name="Première ligne d'adresse")
    line2 = models.CharField(max_length=150, verbose_name="Deuxième ligne d'adresse", null=True, blank=True)
    zipcode = models.IntegerField(verbose_name="Code postal")
    city = models.CharField(max_length=45, verbose_name="Ville")
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.PROTECT, blank=True)

    class Meta:
        app_label = "common"
        verbose_name = "Adresse complète"

    def __str__(self):
        return f"{self.line1} - {self.zipcode} - {self.city}"
