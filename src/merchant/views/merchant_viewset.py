from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from event.models import Event
from event.serializers.events import ListEventSerializer
from merchant.models import Merchant
from merchant.serializers.merchant import MerchantEventSerializer, MerchantRetrieveSerializer
from django.contrib.gis.geos import Point

class MerchantViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Merchant.not_deleted_objects

    serializer_class = MerchantEventSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.action == 'retrieve':
            serializer_class = MerchantRetrieveSerializer

        return serializer_class

    def get_queryset(self):
        return self.get_serializer().setup_for_serialization(self.queryset)


    @action(methods=['GET'], detail=True, url_path='events')
    def get_events(self, request, pk):
        latitude = request.META.get('HTTP_LATITUDE')
        longitude = request.META.get('HTTP_LONGITUDE')
        events = Event.objects_with_mark.filter(merchant=pk)

        if latitude and longitude:
            ref_location = Point(float(longitude), float(latitude), srid=4326)
            events = Event.annotate_distance(events,ref_location)

        events = ListEventSerializer.setup_for_serialization(events)
        return Response(ListEventSerializer(events, many=True).data, status=status.HTTP_200_OK)
