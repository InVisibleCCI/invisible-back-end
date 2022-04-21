from rest_framework_simplejwt.views import TokenObtainPairView

from core.serializers.invisible_token_serializer import InvisibleTokenObtainSerializer


class InvisibleObtainPairView(TokenObtainPairView):
    serializer_class = InvisibleTokenObtainSerializer

