from rest_framework import mixins, viewsets, status

from merchant.models import NavigationTracker
from merchant.serializers.navigation_tracker import NavigationTrackerSerializer


class NavigationTrackerViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = NavigationTracker.objects.all()
    serializer_class = NavigationTrackerSerializer
