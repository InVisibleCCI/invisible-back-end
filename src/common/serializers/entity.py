from rest_framework import serializers

from common.models import Entity


class EntitySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()

    class Meta:
        model = Entity
        fields = (
            'id',
        )
