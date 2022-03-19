from django.db import models

from common.models import Entity, Image
from common.models.adress import Adress


class Merchant(Entity) :
    logo = models.ForeignKey(Image, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10)
    adress = models.ForeignKey(Adress, on_delete=models.CASCADE)
    facebook_url = models.URLField(verbose_name="Lien vers la page facebook", null=True)
    instagram_url = models.URLField(verbose_name="Lien vers la page instagram", null=True)
    twitter_url = models.URLField(verbose_name="Lien vers la page twitter", null=True)
    email = models.EmailField(verbose_name="Adresse Email du marchant",null=True)

    class Meta:
        app_label = "merchant"
        verbose_name = "Marchand"