from rest_framework import serializers

from common.serializers.address import AddressSerializer
from common.serializers.entity import EntitySerializer
from common.serializers.multimedia import ImageSerializer
from event.models import Event
from event.serializers.category import CategorySerializer, AccessibilityCategorySerializer
from event.serializers.review import ReviewsEventSerializer
from merchant.serializers.merchant import MerchantEventSerializer


class ListEventSerializer(EntitySerializer):
    objectID = serializers.UUIDField(source="id")
    name = serializers.CharField()
    difficulty = serializers.IntegerField()
    categories = CategorySerializer(many=True)
    accessibility_categories = AccessibilityCategorySerializer(many=True)
    images = ImageSerializer(many=True)
    address = AddressSerializer()
    average_mark = serializers.FloatField()

    @classmethod
    def setup_for_serialization(cls, queryset):
        return queryset.prefetch_related(
            'categories', 'accessibility_categories', 'images'
        )

    class Meta:
        model = Event
        fields = (
            'objectID',
            'name',
            'difficulty',
            'categories',
            'accessibility_categories',
            'images',
            'address',
            'average_mark'
        )

class RetrieveEventSerializer(ListEventSerializer):
    merchant = MerchantEventSerializer()
    description = serializers.CharField()
    reviews = ReviewsEventSerializer(many=True)
    reviews_count = serializers.IntegerField()

    @classmethod
    def setup_for_serialization(cls, queryset):
        return ListEventSerializer.setup_for_serialization(queryset).prefetch_related(
            'merchant', 'merchant__address', 'reviews__user',
        )

    class Meta:
        model = Event
        fields = ListEventSerializer.Meta.fields + (
            'merchant',
            'description',
            'reviews',
            'reviews_count',
        )

class ListEventFavorites(serializers.ModelSerializer):
    id = serializers.UUIDField

    class Meta:
        model = Event
        fields = (
            'id',
        )
