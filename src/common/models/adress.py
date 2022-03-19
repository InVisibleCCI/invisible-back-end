from common.models import Entity
from core.models import User
from django.db import models


class Adress(Entity) :
    line1 = models.CharField(max_length=150, verbose_name="Première ligne d'adresse")
    line2 = models.CharField(max_length=150, verbose_name="Deuxième ligne d'adresse", null=True)
    zipcode = models.IntegerField(verbose_name="Code postal")
    city = models.CharField(max_length=45, verbose_name="Ville")
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.PROTECT)

    class Meta:
        app_label = "adress"
        verbose_name = "Adresse complète"
