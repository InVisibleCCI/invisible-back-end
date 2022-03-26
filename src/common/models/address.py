import geopy.exc
from django.db import models

from common.geopy.geocoding import GeoCoding
from common.geopy.geopy_custom_exception import LocationNotFound
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

    def set_location_on_save(self):
        geo_coding = GeoCoding()
        address = dict(
            street=self.line1,
            city=self.city,
            postalcode=self.zipcode
        )

        try:
            location = geo_coding.geocode(address)

            if not location:
                address.pop('street')
                # Retry get location without street
                location = geo_coding.geocode(address)

            if location:
                self.latitude = location.latitude
                self.longitude = location.longitude

            if not location:
                raise LocationNotFound("No location for given adresses")

        except geopy.exc.GeocoderTimedOut as e:
            pass

    def save(self, *args, **kwargs):
        if self.user.is_merchant:
            try:
                self.set_location_on_save()
                super(Address, self).save(*args, **kwargs)
            except Exception as e:
                pass

        super(Address, self).save(*args,**kwargs)
