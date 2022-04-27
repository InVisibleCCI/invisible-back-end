from rest_framework import serializers

from common.models import Address


class AddressSerializer(serializers.ModelSerializer):
    line1 = serializers.CharField()
    line2 = serializers.CharField()
    zipcode = serializers.IntegerField()
    city = serializers.CharField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()


    class Meta:
        model = Address
        fields = (
            'line1',
            'line2',
            'zipcode',
            'city',
            'latitude',
            'longitude'
        )
