from event.models import Event
from event.serializers.events import ListEventSerializer
from invisible_backend.settings import ALGOLIA_INDEX


class AlgoliaService:

    @classmethod
    def save_events_to_algolia(cls):
        events = Event.objects.all()
        events = ListEventSerializer.setup_for_serialization(events)
        data = ListEventSerializer(events, many=True).data

        ALGOLIA_INDEX.replace_all_objects(data)
