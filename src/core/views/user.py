from django.http import HttpResponse
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.models import User
from core.serializers.user import UserCreateSerializer, EditUserSerializer, UserRetrieveSerializer


class UserViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet ):
    queryset = User.objects

    def get_serializer_class(self):
        serializer_class = UserCreateSerializer

        if self.action == 'partial_update':
            serializer_class = EditUserSerializer

        return serializer_class

    def create(self, request, *args, **kwargs):
        email = request.data.get('email', None)
        user = User.objects.filter(email=email).first()

        if user:
            return HttpResponse('This user already exists', status=status.HTTP_409_CONFLICT)

        serialized_user = self.get_serializer(data=request.data)
        serialized_user.is_valid(raise_exception=True)
        self.perform_create(serialized_user)
        headers = self.get_success_headers(serialized_user.data)
        return Response(serialized_user.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(methods=['GET'], detail=False, url_path='me', permission_classes=[IsAuthenticated])
    def get_me(self, request):
        user_serialized = UserRetrieveSerializer(request.user).data
        return Response(user_serialized,status=status.HTTP_200_OK)
