from django.contrib.auth.models import Group
from django.db import models
from django.db.models import Manager

from common.models import Entity
from common.views.deleted_manager import NotDeletedManager
from core.models import User


class Merchant(Entity):
    name = models.CharField(max_length=45, default="")
    logo = models.ForeignKey('common.Image', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10)
    address = models.ForeignKey('common.Address', on_delete=models.CASCADE)
    facebook_url = models.URLField(verbose_name="Lien vers la page facebook", null=True, blank=True)
    instagram_url = models.URLField(verbose_name="Lien vers la page instagram", null=True, blank=True)
    twitter_url = models.URLField(verbose_name="Lien vers la page twitter", null=True, blank=True)
    email = models.EmailField(verbose_name="Adresse Email du marchant", null=True, blank=True)
    description = models.TextField(verbose_name="Description du commerçant", null=True, blank=True)
    user = models.ForeignKey(User, related_name='merchant', on_delete=models.CASCADE)

    objects = Manager()
    not_deleted_objects = NotDeletedManager()

    class Meta:
        app_label = "merchant"
        verbose_name = "Marchand"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.user.is_staff = True
        self.user.is_merchant = True
        self.user.groups.add(Group.objects.get(name="Merchant"))
        self.user.save()
        return super(Merchant, self).save(*args, **kwargs)
