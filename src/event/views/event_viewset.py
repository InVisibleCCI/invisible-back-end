from rest_framework import viewsets

from event.models import Event
from event.serializers.events import ListEventSerializer, RetrieveEventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()

    def get_serializer_class(self):
        serializer_class = ListEventSerializer
        if self.action == 'retrieve':
            serializer_class = RetrieveEventSerializer

        return  serializer_class


    def get_queryset(self):
        return self.get_serializer().setup_for_serialization(self.queryset)
