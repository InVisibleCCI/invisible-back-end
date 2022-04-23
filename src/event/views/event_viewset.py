from django.contrib.gis.db.models.functions import GeometryDistance
from django.contrib.gis.geos import Point
from django.db.models import Count
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from common.mixins.viewset import PaginationMixin
from common.pagination import OnStaminaLimitOffsetPagination
from event.models import Event
from event.serializers.events import ListEventSerializer, RetrieveEventSerializer


class EventViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, PaginationMixin, viewsets.GenericViewSet):
    queryset = Event.not_deleted_objects
    pagination_class = OnStaminaLimitOffsetPagination

    def get_serializer_class(self):
        serializer_class = ListEventSerializer
        if self.action == 'retrieve':
            serializer_class = RetrieveEventSerializer

        return serializer_class

    def get_queryset(self):
        return self.get_serializer().setup_for_serialization(self.queryset)

    def list(self, request, *args, **kwargs):
        if request.GET.get('page') == "homepage":
            result = {
                "near_location": [],
                "user_favorites": [],
                "exclusives": [],
                "most_visited": [],
            }
            latitude = request.GET.get('latitude')
            longitude = request.GET.get('longitude')

            if latitude and longitude:
                ref_location = Point(float(longitude), float(latitude), srid=4326)
                near_location = Event.not_deleted_objects.order_by(GeometryDistance("address__location", ref_location))[:4]
                near_location = ListEventSerializer.setup_for_serialization(near_location)
                result['near_location'] = ListEventSerializer(near_location, many=True).data

            if not request.user.is_anonymous:
                user_favorites = ListEventSerializer.setup_for_serialization(Event.not_deleted_objects.filter(user=request.user))
                result['user_favorites'] = ListEventSerializer(user_favorites, many=True).data

            exclusive = RetrieveEventSerializer.setup_for_serialization(Event.not_deleted_objects(is_exclusive=True))
            result['exclusives'] = RetrieveEventSerializer(exclusive, many=True).data

            most_visited = Event.not_deleted_objects.annotate(count_trackers=Count('navigations_trackers_event')).order_by(
                '-count_trackers')[:4]
            most_visited = RetrieveEventSerializer.setup_for_serialization(most_visited)
            result['most_visited'] = RetrieveEventSerializer(most_visited, many=True).data

            return Response(result, status=status.HTTP_200_OK)

        return super(EventViewSet, self).list(request, *args, **kwargs)
