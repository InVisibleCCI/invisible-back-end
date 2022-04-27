from common.serializers.entity import EntitySerializer
from rest_framework import serializers

from event.models import Event
from merchant.models import NavigationTracker, Merchant


class NavigationTrackerSerializer(EntitySerializer):
    event = serializers.CharField(allow_null=True)
    merchant = serializers.CharField(allow_null=True)

    def create(self, validated_data):
        tracker = NavigationTracker.objects.create(
            type=validated_data['type']
        )
        if validated_data['event'] != None:
            tracker.event = Event.objects.filter(id=validated_data['event']).first()

        if validated_data['merchant'] != None:
            tracker.merchant = Merchant.objects.filter(id=validated_data['event']).first()

        tracker.save()

        return tracker

    class Meta:
        model = NavigationTracker
        fields = (
            'type',
            'event',
            'merchant',
        )
