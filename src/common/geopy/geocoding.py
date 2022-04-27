from django.conf import settings
from geopy.geocoders import Nominatim


class GeoCoding:
    geolocator = Nominatim(user_agent=settings.GEOCODE_APP_NAME)

    """
    @param address : dictionnary who specified address line 1,city, and postalcode
    @return : instance of class Geolocation : latitude and longitude
    """
    def geocode(self, address):
        location = self.geolocator.geocode(address)

        if not location:  # Can't locate the address
            return None

        return GeoLocation(location)


class GeoLocation:
    def __init__(self, location):
        self.latitude = location.latitude
        self.longitude = location.longitude
