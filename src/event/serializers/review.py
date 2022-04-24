from rest_framework import serializers

from common.serializers.entity import EntitySerializer
from common.serializers.multimedia import ImageSerializer
from core.models import User
from event.models import Event
from event.models.review import Review

class UserPublicSerializer(serializers.ModelSerializer):
    public_name = serializers.CharField()
    avatar = ImageSerializer()

    class Meta:
        model = User
        fields = (
            'public_name',
            'avatar',
        )

class ReviewsEventSerializer(EntitySerializer):
    title = serializers.CharField()
    description = serializers.CharField()
    mark = serializers.FloatField()
    user = UserPublicSerializer()

    class Meta:
        model = Review
        fields = EntitySerializer.Meta.fields + (
            'title',
            'description',
            'mark',
            'user',
        )

class CreateReviewsEventSerializer(EntitySerializer):
    title = serializers.CharField()
    description = serializers.CharField()
    mark = serializers.FloatField()
    event_id = serializers.CharField()

    def create(self, validated_data):
        # check get request ? user ?
        event = Event.objects.filter(id=validated_data['event_id']).first()
        review = Review.objects.create(
            title=validated_data["title"],
            description=validated_data["description"],
            mark=validated_data["mark"],
            user=self.context['request'].user,
            event=event,
        )

        review.save()
        return review

    class Meta:
        model = Review
        fields = (
            'title',
            'description',
            'mark',
            'event_id',
        )
