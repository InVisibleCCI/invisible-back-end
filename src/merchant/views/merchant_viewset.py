from rest_framework import mixins, viewsets

from merchant.models import Merchant
from merchant.serializers.merchant import MerchantEventSerializer, MerchantRetrieveSerializer


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
