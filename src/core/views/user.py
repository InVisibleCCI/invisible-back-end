from django.utils import timezone
from secrets import token_urlsafe

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from common.mails import send_registration_mail, send_reset_password_mail
from common.models import Image
from core.models import User
from core.serializers.user import UserCreateSerializer, EditUserSerializer, UserRetrieveSerializer
from event.models import Event
from event.serializers.events import ListEventSerializer


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
            return HttpResponse("L'utilisateur existe déjà", status=status.HTTP_409_CONFLICT)

        serialized_user = self.get_serializer(data=request.data)
        serialized_user.is_valid(raise_exception=True)
        self.perform_create(serialized_user)
        send_registration_mail(serialized_user.data)
        headers = self.get_success_headers(serialized_user.data)
        return Response(serialized_user.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        avatar_url = request.data.pop('avatar_url', None)
        if avatar_url:
            new_avatar = Image.objects.create(
                type=4,
                alt_text="avatar de l'utilisateur",
                src=avatar_url
            )
            new_avatar.save()
            request.user.avatar = new_avatar
            request.user.save()

        return super(UserViewSet, self).update(request, *args,**kwargs)

    @action(methods=['GET'], detail=False, url_path='me', permission_classes=[IsAuthenticated])
    def get_me(self, request):
        user_serialized = UserRetrieveSerializer(request.user).data
        return Response(user_serialized,status=status.HTTP_200_OK)



    @action(methods=['GET', 'POST', 'DELETE'], detail=False, url_path='favorites', permission_classes=[IsAuthenticated])
    def manage_favorites(self, request):
        if request.method == "GET":
            events = Event.objects_with_mark.filter(user=request.user)
            events = ListEventSerializer.setup_for_serialization(events)
            events = ListEventSerializer(events, many=True).data
            return Response(events, status=status.HTTP_200_OK)

        event_id = request.data.get('eventId')
        event = Event.objects.filter(id=event_id).first()

        if event is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == "POST" :
            request.user.favorites.add(event)
            return Response(status=status.HTTP_201_CREATED)

        if request.method == "DELETE":
            request.user.favorites.remove(event)
            return Response(status=status.HTTP_204_NO_CONTENT)


    @action(methods=['POST'], detail=False, url_path='send-reset-password-mail')
    def post_send_reset_password_mail(self, request):
        email = request.data.get('email', None)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return HttpResponseNotFound()

        temporary_password = token_urlsafe(12)
        user.set_password(temporary_password)
        user.save()

        user.reset_password_token = token_urlsafe(16)
        user.reset_password_token_end_validity_date = timezone.now() + timezone.timedelta(minutes=15)
        user.save()

        send_reset_password_mail(user,
                                 "InVisible : Demande de modification de mot de passe",
                                 temporary_password)

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['POST'], detail=False, url_path='change-password')
    def post_change_password(self, request):
        old_password = request.data.get('old_password', None)
        new_password = request.data.get('new_password', None)

        if not old_password:
            return HttpResponseBadRequest("Missing old password")

        if not new_password:
            return HttpResponseBadRequest("Missing new password")

        user: User
        if not request.user.is_anonymous:
            user = request.user
        else:
            security_email_token = request.data.get('security_email_token', None)
            if not security_email_token:
                return HttpResponseBadRequest("Missing reset password token")

            user = User.objects.filter(reset_password_token=security_email_token).first()
            if not user:
                return HttpResponseBadRequest("No corresponding user")


        if not user.check_password(old_password):
            return HttpResponseBadRequest("Incorrect old password")

        user.is_active = True
        user.connection_attempt = 0
        user.set_password(new_password)
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)



