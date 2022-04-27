from rest_framework import serializers

from event.models.category import Category


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Category
        fields =  (
            'id',
            'name'
        )

class AccessibilityCategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Category
        fields = (
            'id',
            'name'
        )
