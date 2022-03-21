from django.db import models

from common.models import Entity


class Merchant(Entity):
    name = models.CharField(max_length=45,default="")
    logo = models.ForeignKey('common.Image', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10)
    address = models.ForeignKey('common.Address', on_delete=models.CASCADE)
    facebook_url = models.URLField(verbose_name="Lien vers la page facebook", null=True, blank=True)
    instagram_url = models.URLField(verbose_name="Lien vers la page instagram", null=True, blank=True)
    twitter_url = models.URLField(verbose_name="Lien vers la page twitter", null=True, blank=True)
    email = models.EmailField(verbose_name="Adresse Email du marchant", null=True, blank=True)
    description = models.TextField(verbose_name="Description du commerçant", null=True, blank=True)

    class Meta:
        app_label = "merchant"
        verbose_name = "Marchand"

    def __str__(self):
        return self.name

