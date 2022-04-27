from django.db import models

from common.models.entity import Entity
from django.db.models import Manager

from common.views.deleted_manager import NotDeletedManager

DAYS = [(1, 'Lundi'), (2, 'Mardi'), (3, 'Mercredi'), (4, 'Jeudi'), (5, 'Vendredi'), (6, 'Samedi'),
        (7, 'Dimanche')]


class RegularOpening(Entity):

    merchant = models.ForeignKey('merchant', on_delete=models.CASCADE, blank=True, related_name='regular_openings',
                              verbose_name='Commerçant')

    day = models.IntegerField('jour', choices=DAYS, default=1)
    start_at = models.TimeField('ouverture')
    end_at = models.TimeField('fermeture')

    objects = Manager()
    not_deleted_objects = NotDeletedManager()

    class Meta:
        app_label = "merchant"
        verbose_name = "Horaires d'ouverture"
        ordering = ['start_at', 'day']


    def __str__(self):
        return '{} de {} à {}'.format(DAYS[self.day - 1], self.start_at, self.end_at)
