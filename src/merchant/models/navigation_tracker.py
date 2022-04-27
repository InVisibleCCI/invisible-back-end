from common.models import Entity
from django.db import models

from merchant.models import Merchant

class NavigationChoices(models.IntegerChoices):
    Twitter = 0
    Facebook = 1
    Phone = 2
    Event = 3
    Merchant = 4
    Instagram = 5


class NavigationTracker(Entity):
    type= models.IntegerField(default=-1, choices=NavigationChoices.choices, verbose_name="Type de click")
    merchant = models.ForeignKey(Merchant, models.CASCADE,related_name="navigation_trackers_merchant", null=True)
    event = models.ForeignKey("event.Event", models.CASCADE, related_name="navigations_trackers_event", null=True)
