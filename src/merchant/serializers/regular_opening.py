from rest_framework import serializers

from merchant.models import RegularOpening


class OpeningSerializer(serializers.ModelSerializer):
    start_at = serializers.TimeField(format="%H:%M")
    end_at = serializers.TimeField(format="%H:%M")
    day = serializers.IntegerField()

    class Meta:
        model = RegularOpening
        fields = (
            'start_at',
            'end_at',
            'day',
        )
