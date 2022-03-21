from common.serializers.address import AddressSerializer
from common.serializers.entity import EntitySerializer
from rest_framework import serializers

from common.serializers.multimedia import ImageSerializer
from merchant.models import Merchant


class MerchantEventSerializer(EntitySerializer) :
    name = serializers.CharField()
    logo = ImageSerializer()
    phone_number = serializers.CharField()
    facebook_url = serializers.URLField()
    instagram_url = serializers.URLField()
    twitter_url = serializers.URLField()
    email = serializers.EmailField()
    address = AddressSerializer()

    class Meta:
        model = Merchant
        fields = (
            'name',
            'logo',
            'phone_number',
            'facebook_url',
            'instagram_url',
            'twitter_url',
            'email',
            'address'
        )
