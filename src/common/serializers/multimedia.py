from rest_framework import serializers

from common.models import Image

class ImageSerializer(serializers.ModelSerializer):
    type = serializers.IntegerField()
    order = serializers.IntegerField()
    src = serializers.URLField()
    alt_text = serializers.CharField()

    class Meta:
        model = Image
        fields = (
            'type',
            'order',
            'src',
            'alt_text'
        )


