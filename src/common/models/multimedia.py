from common.models.entity import Entity
from django.db import models


class Multimedia(Entity):
    src = models.URLField(verbose_name="Url du fichier")
    alt_text = models.CharField(max_length=45)

    class Meta:
        abstract = True


class Image(Multimedia):
    class ImageTypeChoices(models.IntegerChoices):
        LOGO = 1, 'Logo'
        BANNER = 2, 'Banner'
        ACTIVITY = 3, "Image de l'expérience"
        AVATAR = 4, "avatar de l'utilisateur"

    type = models.IntegerField(choices=ImageTypeChoices.choices)
