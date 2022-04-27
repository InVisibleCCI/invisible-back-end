from django.contrib.gis.geos import Point
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from common.mixins.viewset import PaginationMixin
from common.pagination import OnStaminaLimitOffsetPagination
from event.models import Event
from event.serializers.events import ListEventSerializer, RetrieveEventSerializer


class EventViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, PaginationMixin, viewsets.GenericViewSet):
    queryset = Event.objects_with_mark
    pagination_class = OnStaminaLimitOffsetPagination

    def get_serializer_class(self):
        serializer_class = ListEventSerializer
        if self.action == 'retrieve':
            serializer_class = RetrieveEventSerializer

        return serializer_class

    def get_queryset(self):
        latitude = self.request.META.get('HTTP_LATITUDE')
        longitude = self.request.META.get('HTTP_LONGITUDE')

        if latitude and longitude:
            ref_location = Point(float(longitude), float(latitude), srid=4326)
            return self.get_serializer().setup_for_serialization(Event.annotate_distance(self.queryset, ref_location))

        return self.get_serializer().setup_for_serialization(self.queryset)

    """
    with homepage parameter get some list of events to display: near location, user favorites, most visited and exclusive
    to get near_location we need to have in request latitude and longitude
    """

    def list(self, request, *args, **kwargs):
        if request.GET.get('page') == "homepage":
            result = {
                "near_location": [],
                "user_favorites": [],
                "exclusives": [],
                "most_visited": [],
            }
            latitude = self.request.META.get('HTTP_LATITUDE')
            longitude = self.request.META.get('HTTP_LONGITUDE')

            if latitude and longitude:
                ref_location = Point(float(longitude), float(latitude), srid=4326)
                result['near_location'] = ListEventSerializer(
                    Event.get_near_location(ref_location, self.get_queryset()), many=True).data

            if not request.user.is_anonymous:
                result['user_favorites'] = ListEventSerializer(Event.get_favorites(request.user, self.get_queryset()),
                                                               many=True).data

            result['exclusives'] = ListEventSerializer(Event.get_exclusives(self.get_queryset()), many=True).data
            result['most_visited'] = ListEventSerializer(Event.get_most_visited(self.get_queryset()), many=True).data

            return Response(result, status=status.HTTP_200_OK)

        return super(EventViewSet, self).list(request, *args, **kwargs)
