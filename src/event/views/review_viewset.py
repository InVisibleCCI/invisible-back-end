from rest_framework import mixins, viewsets

from event.serializers.review import CreateReviewsEventSerializer
from event.models.review import Review
from rest_framework.permissions import IsAuthenticated

class ReviewViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CreateReviewsEventSerializer
    queryset = Review.not_deleted_objects
    permission_classes = [IsAuthenticated]
