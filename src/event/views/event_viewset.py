from django.contrib.gis.db.models.functions import GeometryDistance
from django.contrib.gis.geos import Point
from rest_framework.response import Response
from rest_framework import mixins, viewsets, status

from common.mails import send
from event.models import Event
from event.serializers.events import ListEventSerializer, RetrieveEventSerializer


class EventViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Event.objects.all()

    def get_serializer_class(self):
        serializer_class = ListEventSerializer
        if self.action == 'retrieve':
            serializer_class = RetrieveEventSerializer

        return  serializer_class


    def get_queryset(self):
        return self.get_serializer().setup_for_serialization(self.queryset)

    def list(self, request, *args, **kwargs):
        if request.GET.get('page') == "homepage":
            result = {
                "near_location": dict(),
                "user_favorites": dict(),
                "exclusives" : dict()
            }
            latitude = request.GET.get('latitude')
            longitude = request.GET.get('longitude')

            if latitude and longitude:
                ref_location = Point(float(longitude), float(latitude), srid=4326)
                near_location = Event.objects.all().order_by(GeometryDistance("address__location", ref_location))[:4]
                result['near_location'] = ListEventSerializer(near_location, many=True).data

            if request.user :
                result['user_favorites'] = ListEventSerializer(Event.objects.filter(user=request.user), many=True).data

            result['exclusives'] = ListEventSerializer(Event.objects.filter(is_exclusive=True), many=True).data

            return Response(result, status=status.HTTP_200_OK)

        return super(EventViewSet, self).list(request, *args, **kwargs)
