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


class CommonCategory(Entity):
    name = models.CharField(max_length=20, verbose_name="Nom de la catégorie")

    class Meta:
        abstract = True


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

    type = models.IntegerField(choices=ImageTypeChoices.choices)
